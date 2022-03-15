clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@find . -name ".cache" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -rf htmlcov/
	@rm -f coverage.xml
	@rm -f *.log
	@rm -f *.log.*

flake8:
	@poetry run flake8 --show-source .

check-python-import:
	@poetry run isort --check .

fix-python-import:
	@poetry run isort .

lint: clean flake8 check-python-import
