from celery import Celery

c=Celery('task',broker='redis://192.168.8.130/2')

def fuc():
    return "myfuc"