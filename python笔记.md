[toc]

# python

# 1 环境搭建

# 2 基础语法

# 3 变量

# 4 运算符

# 5 条件语句

# 6 循环语句

# 7 数据及静态方法

## 7.1 数字

## 7.2 字符串

## 7.2.1 split()

切片返回一个字符串列表

```python
str = 'i love fried chicken'
res = str.split(' ')
print(res) # ['i', 'love', 'fried', 'chicken']
```



## 7.3 列表

## 7.4 元组

## 7.5 字典

## 7.6 日期和时间

# 8 函数

# 9 模块

# 10 文件I/O

# 11 File方法

## 11.1 文件执行

同步阻塞

```python
# execfile('test.py') python3已经不支持


with open('test.py','r') as f: 
     exec(f.read())
print("wait or not")

'''
# test.py
import time
time.sleep(5)
'''
```

![image-20200615142007628](C:\Users\43542\Desktop\temp\杂七杂八\python学习\python笔记.assets\image-20200615142007628.png)

# 12 Web

## 12.1 socket服务器搭建

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 创建用于监听连接的套接字
s.bind(('0.0.0.0', 80)) # 绑定监听的IP及端口号
s.listen(5) # 开始监听

while 1:
    conn, addr = s.accept() # 接收客户端的连接, 返回一个用于与客户端通信的新的socket对象
    try:
        buf = conn.recv(1024).decode('utf8') # 将获得的字节形式的字符串解码, 便于后续数据操作
    except:
        print("error")
    else:
        route = buf.split('\r\n')[0].split(' ')[1] # 路由相关
        print(route)
        if route == '/':
            file_path = '/index.html'
        else:
            file_path = route
        try:
            file = open('.' + file_path, 'rb')
        except Exception as e:
            print(e)
        else: 
            # 将获得的静态文件字节数据解码, 便于后续响应体编写
            file_data = file.read().decode('utf8')
            response_start_line = "HTTP/1.1 200 OK\r\n"
            response_headers = "Server: My server\r\n"
            rep = response_start_line + response_headers + "\r\n" + file_data
            # rep = file_dSata
            print(rep)
            file.close()
        
        conn.sendall(bytes(rep, 'utf8')) # 响应体再次编码回应给客户端
        
    conn.close()
```

# 13 正则表达式

## 13.1 规则

- a*    a有0个或多个
- a+    a有至少1个
- [abc]   匹配abc
- [^abc] 匹配除了abc
- .      任意单个字符 除了\n
- ^a   字符串开头a
- $a   字符串结尾a



```python
import re
str = '/test/re.txt'
res = re.match(r'/.+/', str) # r 保持字符串原样, 不进行转义
```

