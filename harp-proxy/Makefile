POETRY ?= $(shell which poetry || echo poetry)

.PHONY: start install test


start: install
	$(POETRY) run harp server --enable harp_benchmark --file config.yml

install:
	$(POETRY) install

test: install
	$(RUN) pytest
