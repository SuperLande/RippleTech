age = int(input("输入您的年龄: "))
vip_level = int(input("输入您的vip等级: "))
if age < 18:
    print("恭喜你可以免费游玩")
elif vip_level >= 3:
    print("恭喜，你可以享受高级会员免费票")
else:
    print("抱歉，您必须支付门票费用")
