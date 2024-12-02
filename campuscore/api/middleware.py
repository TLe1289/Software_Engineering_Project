import json
import logging

from .models import OperationLog

logger = logging.getLogger(__name__)


class UserTypeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Check if the user is a Student
            if hasattr(request.user, "student"):
                request.user_type = "student"
            # Check if the user is a Staff
            elif hasattr(request.user, "staff"):
                request.user_type = "staff"
            # Check if the user is an Instructor
            elif hasattr(request.user, "instructor"):
                request.user_type = "instructor"
            # Fallback if the user doesn't belong to any group
            else:
                request.user_type = "unknown"
        else:
            request.user_type = None  # Anonymous user
        return self.get_response(request)


class LogReadMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.method == "GET" and request.resolver_match:
            try:
                user = request.user if request.user.is_authenticated else None
                model_name = request.resolver_match.view_name
                query_params = request.GET.dict()

                # Ensure all query parameters are serializable
                serialized_params = json.dumps(query_params)

                OperationLog.objects.create(
                    user=user,
                    operation_type="read",
                    model_name=model_name,
                    data_affected=serialized_params,
                )
            except Exception as e:
                # Log the error for debugging
                logger.error(f"Error in LogReadMiddleware: {e}")
                logger.debug(
                    f"Request details: user={request.user}, GET={request.GET}, resolver_match={request.resolver_match}"
                )

        return response
