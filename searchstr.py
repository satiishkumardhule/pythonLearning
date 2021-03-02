
thestring="quick brown fox jumped over the lazy dog "

print(thestring.startswith("the"))
print(thestring.startswith("The"))
print(thestring.endswith("dog "))

print(thestring.find("the"))
print(thestring.rfind("the"))
print("the" in thestring)

print(thestring.replace("lazy","tired"))
print(thestring.count("o"))

from collections import defaultdict 

d=dict()
for a in thestring:d[a]=d.get(a,0)+1
print(d)
    
print(thestring.upper())
print(thestring.lower())
print(thestring.capitalize())

# print(thestring.split(''))

import re

print(re.split(r'\w',thestring))


a=thestring.split()
biggest=max(len(w) for w in a)
print(biggest)

for w in a:
    print(w.ljust(biggest+2,'-'))
    print(w.rjust(biggest+2,'-'))
    print(w.center(biggest+2,'-'))


trans_table=str.maketrans("abcd","1234")
print(str.translate(thestring,trans_table))


a={ i:thestring.count(i) for i in thestring}
print(a)