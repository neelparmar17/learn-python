from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('celery-learn',
            broker= 'amqp://',
            backend = 'amqp://',
            include = ['celery-learn.tasks'])


app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()