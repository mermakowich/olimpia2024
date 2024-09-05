m = [[], []]
tm = []
t = input()
for i in t:
    tm.append(i)
for i in tm:
    if i == "N":
        m[1].append("+")
    if i == "W":
        m[0].append("-")
    if i == "S":
        m[1].append("-")
    if i == "E":
        m[0].append("+")
s1p = 0
s1m = 0
s2p = 0
s2m = 0
for i in m[0]:
    if s1p or s1m or s2p or s2m == 0:
        if i == "+":
            s1p += 1
        if i == "-":
            s1m += 1
for i in m[1]:
    if s1p or s1m or s2p or s2m == 0:
        if i == "+":
            s2p += 1
        if i == "-":
            s2m += 1
# print(s1p)
# print(s1m)
# print(s2p)
# print(s2m)
dl1 = len(m[0])
dl2 = len(m[1])
if (s1p != 0 and s1m != 0 and s2p != 0 and s2m != 0) or (dl1 == 0 and s2p != 0 and s2m != 0) or (dl2 == 0 and s1p != 0 and s1m != 0):
    print("Yes")
else:
    print("No")