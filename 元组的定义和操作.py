# 元组的操作方法：
# 查找 index()
# 统计某个数据出现次数 count()
# 统计元组内的元素个数len()
t8 = ('a', 'b', 'c', 'd')
num = len(t8)
print(f"t8元组中的元素有: {num}个")
# 元组的遍历：while
index = 0
while index < len(t8):
    print(f"元组的元素有: {t8[index]}")
    # 至关重要
    index += 1
# 元组的遍历: for
for element in t8:
    print(f"2元组的元素有: {element}")

# 修改元组的内容
# t8[0] = 'fuck'

# 元组修改的特例，元组里的List
t9 = (1, 2, ['ripplee', 'jack'])
print(t9)
t9[2][1] = 'rose'
print(t9[2][1])