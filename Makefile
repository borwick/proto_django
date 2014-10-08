SHELL=/bin/sh
DJANGO_ENV ?= dev
DJANGO_SETTINGS = proto_django.settings
SUBDIRS = docs
VIRTUALENV_VERSION = 1.10.1
VIRTUALENV_ROOTDIR = ${HOME}/.virtualenvs
VIRTUALENV_ALIAS = proto_django
PYTHON = python

.PHONY: pulldown pushup clean $(SUBDIRS)

help:
	@echo "options: pulldown pushup clean docs"

pulldown: clean
	git pull
	git fetch --tags
	pip install -r requirements/${DJANGO_ENV}.txt
	# Needed for permissions to be created/updated:
	${PYTHON} manage.py migrate
	${PYTHON} manage.py collectstatic --noinput
	cd bin && ./post.sh

pushup:
	test -z "`git status -s`"
	git push --all
	git push origin --tags
	git checkout develop
	git merge master

clean:
	-find . -name '*.pyc' -print0|xargs -0 rm
	-find . -name '*.pyo' -print0|xargs -0 rm
	$(MAKE) -C docs clean

$(SUBDIRS):
	$(MAKE) -C $@ all

virtualenv:
	test ! -d ${VIRTUALENV_ROOTDIR}/${VIRTUALENV_ALIAS}
	bash -l -i -c 'lsvirtualenv > /dev/null'
	wget --no-check-certificate http://pypi.python.org/packages/source/v/virtualenv/virtualenv-${VIRTUALENV_VERSION}.tar.gz
	tar xvf virtualenv-${VIRTUALENV_VERSION}.tar.gz
	${PYTHON} virtualenv-${VIRTUALENV_VERSION}/virtualenv.py --no-site-packages --setuptools ${VIRTUALENV_ROOTDIR}/${VIRTUALENV_ALIAS}
	rm virtualenv-${VIRTUALENV_VERSION}.tar.gz
	rm -rf virtualenv-${VIRTUALENV_VERSION}
	bash -l -i -c 'workon ${VIRTUALENV_ALIAS} && add2virtualenv .'
	bash -l -i -c 'workon ${VIRTUALENV_ALIAS} && pip install -r requirements/${DJANGO_ENV}.txt'
	echo "export DJANGO_ENV='${DJANGO_ENV}'" >> ${VIRTUALENV_ROOTDIR}/${VIRTUALENV_ALIAS}/bin/postactivate
	echo "export DJANGO_SETTINGS_MODULE='${DJANGO_SETTINGS}'" >> ${VIRTUALENV_ROOTDIR}/${VIRTUALENV_ALIAS}/bin/postactivate
	echo "${VIRTUALENV_ALIAS}" > .venv
