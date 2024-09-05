s = input()
m = []
for i in s:
    m.append(i)
d = int(input())
m2 = []
s = 0
zv = 0
for i in m:
    if i != "?" and i != "*":
        m2.append(i)
    if i == "*":
        zv += 1
    if i == "?":
        s += 1
inv = []
inz = []
for i in range(len(m)):
    if m[i] == "?":
        inv.append(i)
    if m[i] == "*":
        inz.append(i)

if d > len(m2) and zv != 0:
    i = inz[0]
    mmm = m2[]

