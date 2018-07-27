.PHONY: all
all:

.PHONY: setup
setup:
	nodenv install --skip-existing
	npm install -g npm
	npm install -g zapier-platform-cli

.PHONY: install
install:
	npm install

.PHONY: test
test:
	zapier test
