from array import array

a= array("i",[1,4,33,2,23,12])
print(a.typecode, a.itemsize)

for i in a:
    a.append(5)

print(a)