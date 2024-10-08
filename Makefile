# Useful for jupyter notebooks
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

SHELL:=/bin/bash
PROJECT=drug_review_analysis
VERSION=3.7.17
VENV=${PROJECT}-${VERSION}
VENV_DIR=$(shell pyenv root)/versions/${VENV}
PYTHON=${VENV_DIR}/bin/python
JUPYTER_ENV_NAME=drug_review_env
JUPYTER_PORT=8888


clean:
	pyenv virtualenv-delete --force ${VENV}
	rm .python-version

requisites: $(UNAME)

Darwin: 
	brew update 
	brew install pyenv pyenv-virtualenv

Linux: 
	git clone https://github.com/pyenv/pyenv.git ~/.pyenv
	echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
	echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
	exec "$SHELL"
	. ~/.bash_profile
	echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile

build:
	$(MAKE) install
	$(MAKE) ipykernel

venv: $(VENV_DIR)

$(VENV_DIR):
	pyenv virtualenv ${VERSION} ${VENV}
	$(PYTHON) -m pip install --upgrade pip
	echo ${VENV} > .python-version

install: venv requirements.txt
	$(PYTHON) -m pip install -r requirements.txt

update: install
	$(PYTHON) -m pip freeze > requirements.txt

ipykernel: venv
	$(PYTHON) -m pip install ipykernel jupyter jupyter_contrib_nbextensions
	$(PYTHON) -m ipykernel install --user --name=$(VENV) --display-name=$(JUPYTER_ENV_NAME)
	$(PYTHON) -m jupyter nbextension enable --py widgetsnbextension --sys-prefix

jupyter: venv
	jupyter notebook --port $(JUPYTER_PORT)

run: build
	$(MAKE) jupyter