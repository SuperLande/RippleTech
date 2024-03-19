# 变量作用域指的是变量的作用范围（变量在哪里可用，那里不可用）
# 主要分为2类：局部变量和全局变量
# 所谓局部变量是定义在函数体内部的变量，即只在函数体内部生效
# 局部变量的作用：在函数体内部

# 局部变量num演示
def test_a():
    num = 100
    print(num)
test_a()
num2 = int(input("请输入一个数字: "))
def test_b():
    print(num2)

def test_c():
    print(num2)
test_b()
test_c()


# 在函数中声明全局变量
def test_d():
    global jack
    jack = int(36)
    print(jack)
test_d()
print(jack)
