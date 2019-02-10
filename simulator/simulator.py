#!/usr/bin/env python3

from urllib import request
from urllib.error import HTTPError
from datetime import datetime
import os, time

print('Starting simulator')

job_name = os.environ['SIMULATOR_JOB_NAME']
pushgateway_url = os.environ['SIMULATOR_PUSHGATEWAY_URL']

target_url = pushgateway_url.rstrip('/') + '/metrics/job/' + job_name

c = 0
while True:
    data = '''\
# TYPE processed_items counter
# HELP processed_items The total number of processed items.
processed_items {processed_items}
'''.format(processed_items=c).encode()
    req =  request.Request(target_url, data=data)
    try:
        resp = request.urlopen(req)
    except HTTPError as err:
        print(f'Failed to push data to pushgateway: {err}')
    time.sleep(5)
    c = c + 1
