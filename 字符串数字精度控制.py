"""
#可以使用"m.n"来控制数据的宽度和精度
#·m，控制宽度，要求是数字
#·n，控制小数点精度，要求是数字，会进行小数的四舍五入
#示例：
#·%5d：表示将整数的宽度控制在5位，如数字11，被设置为5d，就会变成：[空格][空格][空格]11，用3个空格补足宽度。
#·%5.2f：表示将宽度控制为5，将小数点精度设置为2
# 小数点和小数部分也算入宽度计算。如，对11.345设置了%7.2f后，结果是：[空格][空格]11.35。2个空格补足宽度，小数部分限制后2位精度后，四舍五入为.35
#·%.2f：表示不限制宽度，只设置小数点精度为2，如11.345设置为%.2f后，结果是11.35
"""
num1 = 11
num2 = 11.345
message = ("数字11宽度限制5，结果是：%5d" % num1)
print(message)
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制5，结果是：%1d" % num1)
print("数字11.345宽度限制7，小数精度2，结果是: %7.2f" % num2)
print("数字11.345小数精度2，结果是: %.2f" % num2)
