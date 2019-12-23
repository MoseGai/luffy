from .celery import app

@app.task
def low(n1, n2):
    print('减法：%s' % (n1 - n2))
    return n1 - n2
