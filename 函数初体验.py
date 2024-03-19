"""
为什么要学习使用函数？
为了得到一个针对特定需求，可供重复利用的代码段
提高程序的复用性，减少重复性代码，提高开发效率
"""
# name = "ripplee"
# length = len(name)
# print(length)

str1 = "ripplee"
str2 = "is"
str3 = "a good lawyer"

# 定义一个技术的变量
# count = 0
# for i in str1:
#     count += 1
# print(f"字符串str1的长度是{count}")
# print(f"字符串str1的长度是{len(str1)}")

def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是{count}")

my_len(str1)
my_len(str2)
my_len(str3)