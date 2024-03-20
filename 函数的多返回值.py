"""
1.掌握位置参数
根据参数位置来传递参数
2.掌握关键字参数
.通过"键=值"形式传递参数，可以不限参数顺序
.可以和位置参数昏庸，位置参数需在前面
3.掌握缺省参数
.不传递参数值时会使用默认的参数值
.默认值的参数必须定义在最后
4.掌握不定长参数
. 位置不定长传递以*号标记一个形式参数，以元组的形式接受参数，形式参数一般命名为args
· 关键字不定长传递以**号标记一个形式参数，以字典的形式接受参数，形式参数一般命名为kwargs
"""
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

# 不定长参数： 也叫可变参数，用于不确定调用的时候会传递多少个参数的场景
# 作用：当调用函数时不确定参数个数时，可以使用不定长参数
# 不定长参数的类型：
def user3_info(*args):
    print(f"args的参数类型是:{type(args)},内容是{args}")
user3_info(1, 2, 3, '小明', '男孩')

# 关键字传递,kw就是keyword
def user4_info(**kwargs):
    print(f"args的参数类型是:{type(kwargs)},内容是{kwargs}")
user4_info(1, 2, 3, '小明', '男孩')