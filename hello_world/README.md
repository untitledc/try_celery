http://docs.celeryproject.org/en/latest/getting-started/next-steps.html#project-layout

## Start worker
```bash
# Terminal 1
$ .env/bin/celery -A hello_world.celery:app worker -l info --concurrency 3
```

## Execute task
```bash
# Terminal 2
$ .env/bin/python -m hello_world.main
```
