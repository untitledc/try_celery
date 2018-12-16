# -*- coding: utf-8 -*-

from celery import group
from .celery_app import app
from .my_tasks import show


def main():
    # only check availability initially
    if not app.control.inspect().active():
        raise Exception('celery worker not available')

    job = group([
        show.s('t1', 'f1.txt', 12), show.s('t2', 'f2.txt', 11),
        show.s('t3', 'f3.txt', 10), show.s('t4', 'f4.txt', 15),
        show.s('t5', 'f5.txt', 14), show.s('t6', 'f6.txt', 13),
        show.s('t7', 'f7.txt', 21),
        show.s('t8', 'f8.txt', 19), show.s('t9', 'f9.txt', 19),
        show.s('t10', 'f10.txt', 19), show.s('t11', 'f11.txt', 19),
        show.s('t12', 'f12.txt', 19)
    ])

    job_result = job.apply_async()
    print(job_result.ready())
    print(job_result.successful())
    print(job_result.completed_count())
    print(job_result.join())  # don't use .get(), it hangs
    print(job_result.ready())
    print(job_result.successful())
    print(job_result.completed_count())

if __name__ == '__main__':
    main()