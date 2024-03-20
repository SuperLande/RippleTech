# 知道函数如何返回多个返回值
def test_return():
    return 1, 'hello', True
x, y, z = test_return()
print(x)
print(y)
print(z)
# 必须接好值，不能漏接
# 位置参数：调用参数时根据函数定义的参数位置来传递参数
def usr_info(name, age, gender):
    print(f"您的名字是{name},年龄是{age},性别是{gender}")

usr_info('TOM', 20, '男')

# 关键字参数
# 关键字参数：函数调用时通过“键=值”形式传递参数
# 作用：可以让函数更加清晰、容易地使用，同时也清除了参数的顺序需求
def user_info(name, age, gender):
    print(f"您的名字是{name},年龄是{age},性别是{gender}")
# 关键字传参
user_info(name="小明", age=20, gender="男")
# 可以不按照固定顺序
user_info(age=20, name="周庆", gender="男")

# 缺省参数（默认值）
def user2_info(name, age, gender="男"):
    print(f"姓名是: {name}, 年龄是: {age}, 性别是: {gender}")
user2_info('小天', 13)
