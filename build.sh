#!/usr/bin/env bash

curl -sSL https://install.python-poetry.org | python3 -
source $HOME/.local/bin

make install && make collectstatic && make migrate