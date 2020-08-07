#!/usr/bin/env python3
from os import getenv
from os.path import join, dirname

api_key = getenv('API_KEY')
root_url = getenv('API_ROOT_URL')
max_level = int(getenv('MAX_LEVEL'))
