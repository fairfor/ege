#ege 25 №78
c = 0
for k in range(2, 200001):
 
    prime = True
    
    for i in range(2, int(k**0.5)+1):
        if k%i == 0:
            prime = False
            break
 
    if prime:
        c += 1
print(c)
