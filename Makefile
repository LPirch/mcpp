PYTHON ?= python

.PHONY: default build check test-upload upload clean

default: build check

build:
	$(PYTHON) -m build

check:
	twine check dist/*

test-upload: build check
	twine upload -r testpypi dist/*

upload: build check
	twine upload dist/*

clean:
	rm -rf dist build *.egg-info src/*.egg-info
