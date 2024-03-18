"""
continue关键字用于：中断本次循环，直接进入下一次循环
continue可以用于：for循环和while循环，效果一致
"""
"""
演示循环终端语句 continue
for i in range(1, 6):
     print("语句1")
     continue
continue会直接结束本次循环，进行下一次循环
     print("语句2")
continue中断嵌套循环
"""

"""
for i in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        continue
        print("语句3")
    print("语句4")
"""


# Break循环直接导致循环整体结束
for i in range(1,100):
    print("语句1")
    break
    print("sentence2")
print("sentence3")