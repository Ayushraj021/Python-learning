temp = "Hello? how are you?"

if(temp.isdigit()):
    temp += "fine"
else:
    for var1 in range(len(temp)):
        if(temp[var1] == '?'):
            break

    final_val = temp[:var1+1]

    if(final_val.endswith('u')):
        final_val = final_val.replace('you', 'u')
    else:
        final_val = final_val.upper()

print(final_val)
