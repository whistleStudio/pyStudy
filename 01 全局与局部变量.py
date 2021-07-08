# 函数作用域
g = 1
arr = [1, 2]

# 1 对于全局不可变数据，局部作用域内可以打印，但不能进行修改; 需要先在局部作用域内做出global声明，才能进行修改
# 2 对于全局可变数据（引用），直接可以修改
# 3 对于嵌套函数，子作用域如果想要修改父作用域的不可变数据；需要先在父作用域内做出nonlocal声明
# 4 对于嵌套函数，可变数据，仍然是可以直接修改
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

def fun4 ():
    l = 1
    l_arr = [1, 2]
    def inner_fun ():
        nonlocal l
        l += 1
        l_arr[0] = 2
        l_arr.append(3)
        print('---inner---', '\n', l, l_arr)
    inner_fun()

fun4()