# 函数本身，也可以作为参数传入另一个函数
def test_func(compute):
    result = compute(1,2)
    print(result)
def compute(x, y):
    return x + y
test_func(compute)
