import random
num = random.randint(1,100)
circle = 1
#布尔变量决定循环是否继续
flag = True
while flag:
    guess_num = int(input("请输入你的猜测的数字: "))
    if guess_num == num:
        print("猜中了！")
        flag =False
    else:
        if guess_num >= num:
            print("大了！")
        else:
            print("小了！")
        circle += 1
print(f"您一共猜测了{int(circle)}次")