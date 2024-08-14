my_str = "ALL3 that glitters is2 not3 gold4"
my_lst = []

for char in my_str:
    if char.isdigit():
        my_lst.append(int(char))
        my_str = my_str.replace(char, "")

print(my_str, my_lst)
