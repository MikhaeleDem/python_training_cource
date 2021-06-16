'''a = 'c16S5V2C9A7r17I17p1I14W20e14u17I16E5Z7O19V14H13r20B18j10i7o7s15W4U9Z5A18a15'
a += " "
c = "1234567890"
res = ""
count = ""
j = 1

for i in range(len(a) - 1):
    if a[i] not in c:
        res += a[i]

        while a[i + j] in c:
            count += a[i + j]
            j += 1
    else:
        continue
    res += a[i] * (int(count) - 1)
    j = 1
    count = ""
print(res)'''

import math
r = float(input())
p = math.pi
print(2*p*r)