# open()打开函数
# 语法：open(name,mode,encoding)
# mode: r只读，w写入，a追加
# 注意指针
import time

f = open('python.txt', 'r', encoding="UTF-8")
# print(type(f))
# print(f"读取10个字节的结果: {f.read()}")
# 读取文件全部行，封装到列表
# lines = f.readlines()
# print(f"lines对象的类型是{type(lines)}")
# print(f"lines对象的内容是:{lines}")

# 单行读取，封装为字符串
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"lines对象的类型是{type(line1)}")
# print(f"lines对象的内容是:{line1}")
# print(f"lines对象的类型是{type(line2)}")
# print(f"lines对象的内容是:{line2}")
# print(f"lines对象的类型是{type(line3)}")
# print(f"lines对象的内容是:{line3}")

# 每行读取
# for line in f:
#    print(f"每一行数据是:{line}")

# 文件的暂停
time.sleep(500000)

# 文件的关闭
f.close()
time.sleep(500000)

# with open 语法操作文件，执行完语句块后会自动关闭文件，可以避免你遗忘close
with open('python.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        print(f"每一行数据是: {line}")
time.sleep(88888)
