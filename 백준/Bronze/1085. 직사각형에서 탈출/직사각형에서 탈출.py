import sys

def cinput():
    return sys.stdin.readline().rstrip()
"""
                  (w,h)
     (x,y)

(0,0)
"""

x, y , w, h = map(int, cinput().split())

d1 = y
d2 = x
d3 = (w-x)
d4 = (h-y)

min_value = min(d1, d2, d3, d4) 
print(min_value)