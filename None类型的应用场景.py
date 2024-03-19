# None作为一个特殊的字面量，用于表示：空，无意义，有非常多的应用场景
# ·用在函数无返回值上
# ·用在if判断上
#  ·在if判断中，None等同于False
#  ·一般用于在函数中主动返回None，配合if判断做相关处理
# ·用于声明无内容的变量上
#  ·定义变量，但暂时不需要变量有具体值，可以用None来代替
# name = None

#用None做if判断
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None
result = check_age(19)
if not result:
    # 进入if表面result是None值，也就是False
    print("未成年，不得进入")
else:
    print("你已成年，请上机")

# None用于声明无初始值的内容
name = None
