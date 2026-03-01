install:
	@pip install -e .

lint:
	@flake8 gendiff tests

test:
	@python -m pytest

test-coverage:
	@python -m pytest --cov=gendiff --cov-report=xml

.PHONY: install lint test test-coverage