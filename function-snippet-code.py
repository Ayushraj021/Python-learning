def func1():
    print("Inside Func1")
    return 10

def func2():
    print("Inside Func2")
    num=func1()
    return num

def func3():
    print("Inside Func3")
    num=func2()
    num=num*5
    return num

val=func3()
print(val)