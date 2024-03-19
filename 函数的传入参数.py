def add(x,y):
    result = int(x) + int(y)
    print(result)
x = input("请输入x的值: ")
y = input("请输入y的值： ")
add(x,y)

def num(a):
    result = int(a) * 10 + 2 * 90
    print(result)
a = input("请输入a的值: ")
num(a)

"""
函数定义中的参数，称之为形式参数
函数调用中的参数，称之为实际参数
函数的参数数量不限，使用逗号分隔开
传入的时候，要和形式参数一一对应，逗号隔开
"""