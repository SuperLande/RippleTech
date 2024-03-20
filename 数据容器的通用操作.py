# len(容器)
# max(容器)
# min(容器)

my_list = [1, 2, 3, 4, 5, 6]
my_tuple = (1, 2, 3, 4, 5, 6)
my_str = '123456'
my_set = {1, 2, 3, 4, 5, 6}
my_dict = {'key': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5, 'key6': 6}

# len元素个数
print(f"列表 元素个数有： {len(my_set)}")
print(f"元组 元素个数有： {len(my_tuple)}")
print(f"字符串 元素个数有： {len(my_str)}")
print(f"集合 元素个数有： {len(my_set)}")
print(f"字典 元素个数有： {len(my_dict)}")

# max最大元素
print(f"列表 元素个数有： {max(my_set)}")
print(f"元组 元素个数有： {max(my_tuple)}")
print(f"字符串 元素个数有： {max(my_str)}")
print(f"集合 元素个数有： {max(my_set)}")
print(f"字典 元素个数有： {max(my_dict)}")

# min最小元素
print(f"列表 元素个数有： {min(my_set)}")
print(f"元组 元素个数有： {min(my_tuple)}")
print(f"字符串 元素个数有： {min(my_str)}")
print(f"集合 元素个数有： {min(my_set)}")
print(f"字典 元素个数有： {min(my_dict)}")

# 容器的通用转换功能，列表
print(f"列表转列表的结果是{list(my_tuple)}")
print(f"字符串转列表的结果是{list(my_str)}")
print(f"集合转列表的结果是{list(my_set)}")
print(f"字典转列表的结果是{list(my_dict)}")

# 容器的通用转换功能，字符串
print(f"列表转字符串的结果是{str(my_tuple)}")
print(f"字符串转字符串的结果是{str(my_str)}")
print(f"集合转字符串的类型是{type(str(my_set))}")
print(f"字典转字符串的结果是{str(my_dict)}")

# 容器的通用排序功能
# sorted(容器, reverse=True)
# 排序结果会通通变成列表对象
my_list = [3, 1, 2, 5, 4, 7, 7]
my_tuple = (3, 1, 2, 4, 6, 5)
my_str = '9871132'
my_set = {5, 4, 2, 5, 0, 9}
my_dict = {'key': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5, 'key6': 6}
print(f"列表对象的排序结果是: {sorted(my_list)}")
print(f"字符串对象的排序结果是: {sorted(my_str)}")
print(f"集合对象的排序结果是: {sorted(my_set)}")
print(f"字典对象的排序结果是: {sorted(my_dict)}")
print(f"列表对象的反向排序结果是: {sorted(my_list, reverse=True)}")
print(f"字符串对象的反向排序结果是: {sorted(my_str, reverse=True)}")
print(f"集合对象的反向排序结果是: {sorted(my_set, reverse=True)}")
print(f"字典对象的反向排序结果是: {sorted(my_dict, reverse=True)}")