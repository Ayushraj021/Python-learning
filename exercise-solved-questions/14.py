var1 = 0
var2 = 10

while var1 <= 10 and var2 >= 1:
    print(var1, var2)
    var2 = var2 - 1
    var1 = var1 + 1
    if var1 == var2:
        break
