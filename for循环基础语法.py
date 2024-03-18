"""
for循环，遍历循环
与while不同，for循环是无法定义循环条件的
只能从被处理的数据集中，依次取出内容进行处理
理论上，python的for循环无法构建无限循环（被处理的数据机不可能无限大）
即for循环无法构建无限循环
"""

name = "rippppplee"
num = 0
for x in name:
    if x == "p":
        num += 1
print(num)
