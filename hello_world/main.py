# -*- coding: utf-8 -*-

from hello_world.celery import app
from hello_world.tasks import add


def main():
    # only check availability initially
    if not app.control.inspect().active():
        raise Exception('celery worker not available')
    r = add.delay(23, 45)
    print(r.get())


if __name__ == '__main__':
    main()