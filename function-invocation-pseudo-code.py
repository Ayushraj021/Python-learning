#Code1
print("code-1")
def func6(a,b,c):
    res_avg=(a+b+c)/3
    return res_avg
print("1st invocation of code-1")
func6(6,8,10)
print("returned value is not assigned to any variable")

print("------------------------------------------------")
print("2nd invocation of code-1")
average=func6(10,15,20)
print("returned value assigned to a variable")
print("value of variable, average:", average)

print("------------------------------------------------")
print("3rd invocation of code-1")
print("returned value is directly printed")
print(func6(1,2,3))



#Code2
print("------------------------------------------------")
print("code-2")
print("------------------------------------------------")
def func7(a,b):
    if(a>b):
        return True
    return False
x=5
y=6

print("1st invocation of code-2")
if(func7(x,y)):
    print("inside if block")
else:
    print("inside else block")


x=6
y=5
print("------------------------------------------------")
print("2nd invocation of code-2")
if(func7(x,y)):
    print("inside if block")
else:
    print("inside else block")

