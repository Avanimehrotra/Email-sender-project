# backend/celery_app.py
from celery import Celery

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    return celery

# This function returns the Celery instance
celery = None
def init_celery(app):
    global celery
    if celery is None:
        celery = make_celery(app)
    return celery
