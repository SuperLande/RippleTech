# 什么是返回值？
# 帮我买3瓶可乐,其中3瓶可乐是参数
# 收到的3瓶可乐，就是返回值
"""
语法格式：
def 函数(参数...):
    函数体
    return 返回值
变量 = 函数(参数)
"""

def add(a,b):
    result = a + b
# 通过返回值，把结果返回给调用者
    return result
# 函数体遇到return关键字，此时已经拦截
#    print("我完事了")
r = add(1, 2)
print(r)
print(type(r))
