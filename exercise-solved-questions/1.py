import math

temp = ['Mysore', 'Bangalore', 'Pune', 'Chennai']

temp.sort()

count1 = len(temp[0])

count2 = len(temp[-1])

final_val = math.ceil(count1 / count2)

print(final_val)
