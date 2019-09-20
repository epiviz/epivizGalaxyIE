#!/bin/bash

python /srv/epiviz.py &

cd /html
python -m http.server &