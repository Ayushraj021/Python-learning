name1 = "Roger"
name2 = "Robert"

def swap_names(name1, name2):
    temp = name1
    name1 = name2
    name2 = temp
    # This function only swaps local variables and does not affect the global variables

print("Before swapping: name1=" + name1 + " name2=" + name2)
swap_names(name1, name2)
print("After swapping: name1=" + name1 + " name2=" + name2)
