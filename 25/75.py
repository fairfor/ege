#ege25 №75
ls = []
for i in range(1000, 20001):
    sm = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            sm += j
    if i - sm == 1:
        ls.append(i)
print(*ls, sep='\n')
