install: #poetry install
	poetry install;

build:
	poetry build;

publish:
	poetry publish --dry-run


package-install:
	python3.9 -m pip install hexlet_code-0.1.0-py3-none-any.whl

package-upgrade:
	python3.9 -m pip install --upgrade --user dist/hexlet_code-0.1.0-py3-none-any.whl;


make lint:
	poetry run flake8 gendiff;