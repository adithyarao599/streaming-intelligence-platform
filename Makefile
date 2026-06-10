install:
	pip install -r requirements.txt

test:
	pytest -v

format:
	black .

lint:
	isort .

run:
	python -m app.main
