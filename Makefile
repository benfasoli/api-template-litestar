.PHONY: help
help:  ## Print available options.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: all
all: install check infra test  ## Install and run all checks.

.PHONY: build
build: ## Build docker image.
	@docker build -t api-template-litestar .

.PHONY: check-format
check-format:  ## Verify code formatting compliance.
	@.venv/bin/ruff format --check src tests

.PHONY: check-lint
check-lint:  ## Verify code compliance with linting rules.
	@.venv/bin/ruff check src tests

.PHONY: check-types
check-types:  ## Verify code types are compliant
	@.venv/bin/mypy src tests

.PHONY: check
check: check-format check-lint check-types ## Run static analysis formatting, linting, and type checks.
	
.PHONY: clean
clean: clean-infra  ## Remove development artifacts and containers.
	@rm -fr .venv
	@rm -fr build
	@find . -name '*~' -exec rm -f {} +
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name '__pycache__' -exec rm -fr {} +
	@find . -name '.coverage' -exec rm -fr {} +
	@find . -name '.mypy_cache' -exec rm -fr {} +
	@find . -name '.pytest_cache' -exec rm -fr {} +
	@find . -name '.ruff_cache' -exec rm -fr {} +

.PHONY: clean-infra
clean-infra:  ## Stop local infrastructure background containers.
	@docker compose down

.PHONY: infra
infra:  ## Start local infrastructure containers in background.
	@docker compose up --remove-orphans --force-recreate --build -d

.PHONY: install
install:  ## Install development dependencies.
	@python3.12 -m venv .venv
	@.venv/bin/pip install .[dev]

.PHONY: format
format:  ## Autoformat source code.
	@.venv/bin/ruff format src

.PHONY: start-dev
start-dev: infra  ## Run local development webserver in debug mode.
	@echo
	@echo 🚀 Visit the OpenAPI Swagger docs: http://127.0.0.1:8000/schema
	@echo
	@.venv/bin/dotenv --file .env.local run -- .venv/bin/litestar --app=src.app:init_app run --debug --reload

.PHONY: test
test:  ## Run tests.
	@.venv/bin/pytest --durations=0 --cov-report=term-missing --cov=src --cov=tests

.PHONY: version
version:  ## Print current version from pyproject.toml to stdout
	@.venv/bin/python -m src.version
