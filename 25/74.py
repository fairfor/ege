#ege 25 №74
cnt = 0
for i in range(2, 30001):
    sm = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            sm += j
    if sm < i:
        cnt += 1
print(cnt)
