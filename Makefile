PYTHON ?= python

.PHONY: default build check test-upload upload clean help

# Show this help.
help:
	@awk '/^#/{c=substr($$0,3);next}c&&/^[[:alpha:]][[:alnum:]_-]+:/{print substr($$1,1,index($$1,":")),c}1{c=0}' $(MAKEFILE_LIST) | column -s: -t

# build and check the package
default: build check

# build the package
build:
	$(PYTHON) -m build

# check the package
check:
	twine check dist/*

# upload the package to testpypi
test-upload: build check
	twine upload -r testpypi --config-file .pypirc dist/*

# upload the package to pypi
upload: build check
	twine upload --config-file .pypirc dist/*

# clean the build files
clean:
	rm -rf dist build *.egg-info src/*.egg-info
