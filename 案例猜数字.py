num = 5
guess = int(input("请猜一个数字: "))
if guess == num:
    print("恭喜，猜对了！")
elif int(input("再猜一个数字: ")) == num:
    print("恭喜，猜对了！")
else:
    print("抱歉，你已经没有机会了!")