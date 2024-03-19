# 如果函数没有是用return语句返回数据，函数是否有返回值
# 实际上是有的
def say_hello():
    print("Hello......")

# 使用变量接受say_hello的返回值
result = say_hello()
# 打印返回值
print(result)
# 打印返回值类型
print(type(result))
