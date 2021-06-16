from math import ceil
from math import floor

d1, v1, d2, v2, p = map(int, input().split())

if d1 > d2:
    v = v1
else:
    v = v2

dmax = max(d1, d2)
dmin = min(d1, d2)
e = dmin - 1
d1 = (dmax - dmin) + 1
d2 = 1
c = d1 - d2

d = (p + (c * v)) / (v1 + v2)
d = ceil(d)
total = d + e

print(total)
