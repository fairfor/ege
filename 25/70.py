#ege 25 №70
ls = []
lsc = []
for i in range(2, 10001):
    sm = 0
    c = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            c += 1
            sm += j
    if sm == i:
        ls.append(i)
        lsc.append(c)
for w in range(len(ls)):
    print(ls[w], lsc[w])
