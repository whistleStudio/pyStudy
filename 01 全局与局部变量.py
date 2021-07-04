# 函数作用域
g = 1
arr = [1, 2]

# 对于不可变数据，局部作用域内可以打印，但不能进行修改; 需要先在局部作用域内作出global声明，才能进行修改
# 对于可变数据（引用），直接可以修改
def fun1 ():
    print(g)
    print(arr)
fun1()

# def fun2 ():
#     g += 1
#     print(g)
# fun2()

def fun3 ():
    global g
    arr[0] = 2
    g += 1
    print(g)
    print(arr)
fun3()
