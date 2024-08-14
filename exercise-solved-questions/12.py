var1=7
var2=6 
var3=3

print((var1+var2)>(var3) and (var1*var2+var3)>=(var3+var1))

print((var1*var2)>(var3*var1) and (var1*var2)<=(var1*var2*var3))

print((var1*var3)>(var1*var2*var3) or (var1*var3)<=(var2*var3))

print(not((var1*var3)>(var3*var1) and (var1*var3)<=(var2*var3))) 