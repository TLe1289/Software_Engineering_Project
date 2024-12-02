import datetime
import json

from django.core.serializers.json import DjangoJSONEncoder
from django.db import connection
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.forms.models import model_to_dict

from .models import OperationLog


def is_migration():
    """
    Checks if the current operation is being run as part of a migration.
    """
    from django.db.migrations.executor import MigrationExecutor

    try:
        executor = MigrationExecutor(connection)
        return True
    except:
        # If the MigrationExecutor raises an error, it is not a migration
        return False


def serialize_instance(instance):
    """Helper function to serialize a model instance into JSON-serializable format."""
    data = model_to_dict(instance)
    for field, value in data.items():
        if isinstance(value, (datetime.date, datetime.datetime)):
            data[field] = value.isoformat()  # Convert datetime to ISO 8601 string
    return data


@receiver(pre_save)
def log_update_or_create(sender, instance, **kwargs):
    if (
        sender._meta.app_label != "admin" and not is_migration()
    ):  # Exclude admin models and migrations
        user = getattr(instance, "_user", None)  # User must be set in the view
        model_name = sender.__name__
        operation_type = "update" if instance.pk else "create"

        if operation_type == "update":
            old_instance = sender.objects.filter(pk=instance.pk).first()
            old_data = serialize_instance(old_instance) if old_instance else {}
        else:
            old_data = {}

        # Current instance data
        new_data = serialize_instance(instance)

        OperationLog.objects.create(
            user=user,
            operation_type=operation_type,
            model_name=model_name,
            data_affected="N/A",  # Optionally specify affected fields
            old_value=json.dumps(old_data, cls=DjangoJSONEncoder),
            new_value=json.dumps(new_data, cls=DjangoJSONEncoder),
        )


@receiver(pre_delete)
def log_delete(sender, instance, **kwargs):
    if (
        sender._meta.app_label != "admin" and not is_migration()
    ):  # Exclude admin models and migrations
        user = getattr(instance, "_user", None)  # User must be set in the view
        model_name = sender.__name__

        # Serialize instance data
        data = serialize_instance(instance)

        OperationLog.objects.create(
            user=user,
            operation_type="delete",
            model_name=model_name,
            data_affected=json.dumps(data, cls=DjangoJSONEncoder),
        )
