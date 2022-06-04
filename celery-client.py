from celery_server.tasks import asyncRun

# r = test.delay(1,2)
# r2 = test.delay(1,2)

r = asyncRun.delay("13809213237")
print(r.get())
