#!/usr/bin/bash

curl -O https://data.iana.org/TLD/tlds-alpha-by-domain.txt
python3 -m venv venv
. venv/bin/activate
pip install dnspython

python3 ./check-for-caa.py | tee check.txt
