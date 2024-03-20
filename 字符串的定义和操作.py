# 字符串的特点
# 作为数据容器，字符串有如下特点：
# · 只可以存储字符串
# · 长度任意（取决于内存大小）
# · 支持下标索引
# · 允许重复字符串存在
# · 不可用修改
# · 支持for循环
# 字符串的下标
name = 'ripplee'
print(name[0])
# index
print(name.index('p'))
# 字符串取值
name2 = name[-4]
print(f"从字符串{name}取下标为-4的元素，值是: {name2}")
# replace
new_name = name.replace('pp', 'ee')
print(new_name)
# split
name = "jack love rose"
name_list = name.split(" ")
print(f"将字符串{name}进行split切分后，得到: {name_list}， 类型是{type(name_list)}")
# strip方法: 字符串的规整操作
name = " jack love rose "
print(name.strip('j'))
print(name.strip())
# 统计字符串中某个字符串出现的次数
print(name.count('o'))
# 统计字符串的长度
print(len(name))
