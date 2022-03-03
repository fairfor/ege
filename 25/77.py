#ege 25 №77
c = 0
for k in range(2, 20001):
 
    prime = True
    
    for i in range(2, k):
        if k%i == 0:
            prime = False
            break
 
    if prime:
        c += 1
print(c)
