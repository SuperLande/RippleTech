import random
# 构建随机变量
num = random.randint(1, 10)
guess_number = int(input("输入你要猜测的数字: "))
if guess_number == num:
    print("恭喜，第一次就猜中了！")
else:
    if guess_number > num:
        print("你猜测的数字大了！")
    else:
        print("你猜测的数字太小了")

    guess_number = int(input("请再次输入你要猜测的数字: "))

    if guess_number == num:
        print("恭喜，第二次猜中了")
    else:
        if guess_number > num:
            print("你猜测的数字大了！")
        else:
            print("你猜测的数字太小了")

    guess_number = int(input("请再次输入你要猜测的数字: "))
    if guess_number == num:
        print("恭喜，第三次猜中了")
    else:
        print("抱歉，你的三次机会用完了！")
