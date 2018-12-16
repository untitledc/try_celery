# -*- coding: utf-8 -*-

from celery import Celery

app = Celery('proj',
             broker='redis://localhost',
             backend='redis://localhost',
             include=['hello_world.tasks'])

# app.conf.update(
#    broker_transport_options={'visibility_timeout': 10},
# )

if __name__ == '__main__':
    app.start()
