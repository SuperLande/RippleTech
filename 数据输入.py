"""
演示Python的input语句
获取键盘的输入信息
"""
print("请告诉我你是谁: ")
name = input()
print("Get!!!，你是%s!" % name)
print(f"Get!!!，你是{name}!")
# 输入数字类型
num = input("请告诉我你的银行密码: ")
# 数据类型转换为整数
num = int(num)
# 数据类型转换为浮点数
num = float(num)
print("你的银行密码类型是: ", type(num))
