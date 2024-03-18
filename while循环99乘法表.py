"""
Print语句不换行实现方式(传参功能)
print("hello", end="")
print("world", end="")
制表符知识点，自动对齐
print("Hello\tword")
print("Ripplee\thandsome")
"""
# 定义外层的控制变量
row = 1
while row <= 9:
    # 定义内层循环的控制变量
    columns = 1
    while columns <= row:
        # 内层循环的print语句，不要换行，通过\t制表符对齐
        print(f"{row} * {columns} = {row * columns}\t", end="")
        columns += 1
    row += 1
    print()
