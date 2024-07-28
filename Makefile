.PHONY: setup format lint test coverage clean run

setup:
		pip install -r requirements.txt

format:
		isort .
		black .

lint:
		pylint **/*.py

test:
		pytest

coverage:
		pytest --cov=. --cov-report=html

clean:
		find . -type f -name "*.pyc" -delete
		find . -type d -name "__pycache__" -delete
		rm -rf .pytest_cache
		rm -rf htmlcov
		rm -f .coverage

run:
		uvicorn main:app --reload
