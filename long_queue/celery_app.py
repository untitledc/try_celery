# -*- coding: utf-8 -*-

from celery import Celery

app = Celery('proj',
             broker='redis://localhost',
             backend='redis://localhost',
             include=['long_queue.my_tasks'])

app.conf.update(
    worker_prefetch_multiplier=1,
    worker_max_tasks_per_child=100
)

if __name__ == '__main__':
    app.start()
