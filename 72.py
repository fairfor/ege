#ege 25 №72
k = 0
mn = 2000000
mnc = 0
for i in range(2, 20001):
    t = 0
    for j in range(2, i):
        if i % j == 0:
            f = True
            for l in range(2, int(j**0.5)+1):
                if j % l == 0:
                    f = False
                    break
            if f:
                t+=1
                if mn > j:
                    mn = j
                    mnc = t
print(mn, mnc)
