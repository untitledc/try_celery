http://docs.celeryproject.org/en/latest/userguide/canvas.html#groups

## Start worker
```bash
# Terminal 1
$ .env/bin/celery -A long_queue.celery_app:app worker -l debug --concurrency 3 -Ofair 
```

## Execute task
```bash
# Terminal 2
$ .env/bin/python -m long_queue.main
```

## Inspect queue
```bash
$ .env/bin/celery -A long_queue.celery_app:app inspect scheduled
$ .env/bin/celery -A long_queue.celery_app:app inspect active
$ .env/bin/celery -A long_queue.celery_app:app inspect reserved
```

(When worker process is dead) purge queue
```bash
$ .env/bin/celery -A long_queue.celery_app:app purge
```


