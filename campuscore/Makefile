.PHONY: build flush_db load_fixtures run_server collect_static

# Variables
PYTHON=python3
VENV_PYTHON=.venv/bin/python
VENV_PIP=.venv/bin/pip
MANAGE=manage.py

# Build the app
build:
	$(PYTHON) -m venv .venv
	$(VENV_PIP) install -r requirements.txt
	npm install
	npm run build

# Collect static files
collectstatic:
	$(VENV_PYTHON) $(MANAGE) collectstatic --no-input

# Create migrations and apply them
migrations:
	$(VENV_PYTHON) $(MANAGE) makemigrations
	$(VENV_PYTHON) $(MANAGE) migrate --no-input

# Flush the database
flush:
	$(VENV_PYTHON) $(MANAGE) flush --no-input

# Load fixtures
loaddata: flush
	$(VENV_PYTHON) $(MANAGE) loaddata api/fixtures/users.yaml
	$(VENV_PYTHON) $(MANAGE) loaddata api/fixtures/school_data.yaml

# Run the server
run:
	$(VENV_PYTHON) $(MANAGE) runserver

# Run tests
test:
	$(VENV_PYTHON) $(MANAGE) test api

# Format code
format:
	$(VENV_PYTHON) -m black manage.py
	$(VENV_PYTHON) -m black api
	$(VENV_PYTHON) -m black campuscore
	$(VENV_PYTHON) -m isort .
