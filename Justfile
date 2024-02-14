set shell := ["bash", "-uc"]

dev:
    nodemon --watch chatwoot_client --ext py,json --exec poetry run python -m chatwoot_client

publish:
    poetry publish --build

install:
    poetry install

run:
    poetry run python -m chatwoot_client

test:
    pytest -vv

