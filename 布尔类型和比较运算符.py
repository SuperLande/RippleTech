"""
Bool运算，即True or False
运算符
== 判断内容是否相等
!= 判断内容是否不等
> 是否大于
< 是否小于
>= 是否大于等于
<= 是否小于等于
"""
# 定义变量储存布尔类型的数据
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是: {bool_1}, 类型是{type(bool_1)}")
print(f"bool_1变量的内容是: {bool_2}, 类型是{type(bool_2)}")
# 演示进行内容的相等比较
num1 = 10
num2 = 15
print(f"10 == 15的结果是{num1 == num2}")
print(f"10 != 15的结果是{num1 != num2}")
name1 = "itecast"
name2 = "itripplee"
print(f"itcast == itripplee的结果是{name1 == name2}")
# 演示大于小于，大于等于小于等于的比较运算
num1 = 10
num2 = 5
print(f"10 > 5的结果是{num1 > num2}")
print(f"10 < 5的结果是{num1 < num2}")
num1 = 10
num2 = 10
print(f"10 >= 10的结果是{num1 >= num2}")
print(f"10 <= 10的结果是{num1 <= num2}")
num1 = 10
num2 = 11
print(f"10 >= 11的结果是{num1 >= num2}")
print(f"10 <= 11的结果是{num1 <= num2}")