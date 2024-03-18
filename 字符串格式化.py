"""
#Python中3种占位符
#%s：将内容转换成字符串，放入占位位置
#%d：将内容转换成整数，放入占位位置
#%f：将内容转换成浮点型，放入占位位置
"""

name = "ripplee"
message = "I love %s" % name
print(message)
lawfirm = "Yundao"
carrer = "Lawyer"
message2 = "I am a %s in %s" % (carrer, lawfirm)
print(message2)

year_num = 57
avg_salary = 2500
message3 = "杭州实习律师，%s年的平均工资是%s" % (year_num, avg_salary)
print(message3)

firm_name = "允道律师事务所"
setup_year = 2016
avg_salary2 = 8000.99
message4 = "%s,成立于: %d年,人均收入%f元" % (firm_name, setup_year, avg_salary2)
print(message4)
