.PHONY: venv-install
venv-install:
	pip install pipenv==2018.11.26 --user && pipenv install && pipenv run python -m spacy download pt && exit

