var = 200

if var > 200:
    print("Within first block")
    if var == 150:
        print("which is 150")
    elif var == 100:
        print("which is 100")
elif var > 50:
    print("Within second block")
    if var % 50 == 0:
        print("Which is multiple of 5")
    elif var % 100 == 0:
        print("Which is multiple of 10")
    else:
        print("Neither multiple of 5 nor multiple of 10")
else:
    print("Could not find true expression")

print("Good bye!")
