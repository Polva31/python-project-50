install:
	@pip install -e .

lint:
	@flake8 gendiff tests

test:
	@pytest

test-coverage:
	@pytest --cov=gendiff --cov-report=xml

.PHONY: install lint test test-coverage