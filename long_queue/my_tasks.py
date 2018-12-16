# -*- coding: utf-8 -*-

import time
from celery.exceptions import SoftTimeLimitExceeded
from .celery_app import app


@app.task(soft_time_limit=20)
def show(text, filename, sleep_sec=10):
    try:
        print('In ({})'.format(text))
        time.sleep(sleep_sec)
        with open(filename, 'w') as f:
            f.write(text+'\n')
        print('End ({})'.format(text))
        return 'r'+text
    except SoftTimeLimitExceeded as e:
        print(str(e))
