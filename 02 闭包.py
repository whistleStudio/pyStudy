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
函数同样是对象，有一个隐藏属性[[scope]](作用域)，其中储存了函数在创建与执行调用时的上下文集合，且呈链式分布.
每次新的声明定义都会开辟新的内存空间
查找变量原则：从作用域链的顶端依次向下查找

1) fun定义时，
   fun[[scope]] = {
       0: [globals]
   }
2）fun执行时，
    fun[[scope]] = {
        0: [n, a, s, inner_fun],    # 执行完成时，0项被销毁
        1：[globals]
    }
3) inner_fun定义时，
    inner_fun = {
        0: [n, a, s, inner_fun],
        1: [globals]
    }
4) inner_fun执行时，
    inner_fun = {
        0: [b],     # 执行完成时，0项被销毁
        1: [n, a, s, inner_fun],
        2: [globals]
    }

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
