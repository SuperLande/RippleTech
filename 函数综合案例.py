# 函数综合案例
# 要求：做一个ATM取钱机器

# 定义全局变量 moeny name
money = 5000000
name = None
# 要求客户输入姓名
name = input("请输入您的姓名: ")
# 定义查询函数
def query(show_header):
    if show_header == True:
        print("--------查询余额--------")
    print(f"{name}, 您好，您的余额：{money}元")
# 定义存款函数
def saving(num):
    global money
    money += num
    print("--------存款--------")
    print(f"{name},您好，您存款{num}元成功")
    # 调用查询函数
    query(False)
# 定义取款函数
def get_money(num):
    global money
    money -= num
    print("--------取款--------")
    print(f"{name},您好，您取款{num}元成功")
    # 调用查询函数
    query(False)
# 主菜单函数
def main():
    print("--------主菜单--------")
    print(f"{name}您好，欢迎来到银行，请选择操作")
    print("查询余额\t输入1")
    print("存款\t\t输入2")
    print("取款\t\t输入3")
    print("退出\t\t输入4")
    return input("请输入你的选择")

# 设置无限循环，确保程序不退出
while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True)
        continue
    elif keyboard_input == "2":
        num = int(input("存款金额: "))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("取款金额: "))
        get_money(num)
        continue
    else:
        print("感谢使用傻逼ATM，欢迎下次光临")
        break