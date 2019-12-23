from.celery import app


# 一个任务就是一个功能函数，任务的执行结果就是函数的返回值
@app.task
def add(n1,n2):

    print("运算数",n1,n2)
    print("运算结果：%s"%(n2+n1))
    return n1+n2



