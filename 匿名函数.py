# lambda匿名函数
# def关键字，可以定义有名函数
# lambda关键字，可以定义匿名函数（无名称）
# 语法： lambda 传入参数: 函数体(一行代码)
def test_func(compute):
    result = compute(1, 2)
    print(result)

test_func(lambda x, y: x + y)
