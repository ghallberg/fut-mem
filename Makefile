run:
	poetry run python run.py

test:
	poetry run pytest

lint:
	poetry run black .
	poetry run isort .
