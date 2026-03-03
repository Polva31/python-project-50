install:
	pip install --upgrade pip
	pip install -e .

test:
	pytest -vv

lint:
	ruff check .

.PHONY: install test lint
