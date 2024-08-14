code = "jack-and-jill went up the hill"

# Split the code into words and iterate over them
for temp in code.split():
    if temp.endswith("ill"):
        print("Count:", code.count("ill"))
        break

# Replace 'j' with 'm'
code = code.replace("j", "m")

# Split the modified code into words and iterate over them
for temp in code.split():
    if len(temp) % 2 != 0:
        temp_string = str(temp)
        code = code.replace(temp_string, temp_string.upper())

print(code)
