# 定义一个参数, 名称任意，接受一个参数传入（数字类型，表示体温）
# 在函数内进行体温判断（正常范围：小于等于37.5度），并输出相应内容：

# 定义函数，接收1个形式参数，数字类型，表示体温
def temperture(num):
    if float(num) <= 37.5:
        print("请通过闸机口")
    else:
        print(f"你的体温异常，已经达到{num}度请自行隔离，")
# 调用函数，传入实际参数
num = input("请输入你测量出的体温结果： ")
temperture(num)


