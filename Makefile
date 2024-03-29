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
check: check-format check-lint check-types ## Run static format, linting, and type checks.
	
.PHONY: clean
clean: clean-infra  ## Remove development artifacts and containers.
	@rm -f .coverage
	@rm -rf .mypy_cache
	@rm -rf .pytest_cache
	@rm -rf .ruff_cache
	@rm -rf .venv
	@rm -rf build
	@rm -rf `find . -name __pycache__`
	@rm -rf `find . -name *.egg-info`
	@rm -f `find . -type f -name '*~'`
	@rm -f `find . -type f -name '*.pyc'`
	@rm -f `find . -type f -name '*.pyo'`

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
	@.venv/bin/dotenv --file .env.local run --\
		.venv/bin/litestar --app=src.app:app run --debug --reload

.PHONY: test
test:  ## Run tests.
	@.venv/bin/pytest --durations=0 \
		--cov-report=term-missing --cov=src --cov=tests

.PHONY: version
version:  ## Print current version from pyproject.toml to stdout
	@yq -oy '.project.version' pyproject.toml
