list1 = [1, 2, 1, 3, 3, 1, 2, 1, 2, 1]

tuple1 = ("A", "B", "C", "D")
tuple1 += ("E",)

list2 = []

for var1 in range(5, len(list1)):
    list2.append(list1[var1 - 5] + list1[var1])

for var1 in range(len(list2)):
    print(tuple1[var1], list2[var1])
