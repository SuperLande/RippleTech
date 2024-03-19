# 掌握函数嵌套调用
# 函数嵌套调用的执行流程
def func_a():
    print("--2--")
def func_b():
    print("--1--")
    func_a()
    print("--3--")
func_b()