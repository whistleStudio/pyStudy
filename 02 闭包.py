'''
闭包：
1 格式：
def fun():
    ...
    def inner_fun():
        ...
    return inner_fun
2 作用：将父级变量私有化，且不会因为调用结束销毁
'''

'''
用js解释整个过程

'''
def fun(n):
    a = 1
    s = 0
    def inner_fun():
        nonlocal s
        b = 2
        s += a + b + n
        b += 1
        print(s)
        # print(locals())
    # print(locals())
    return inner_fun
# print(globals())
inc = fun(1)
inc()
inc()
