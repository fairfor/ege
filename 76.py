#ege25 №76
def divisors(number):
    return sum(x for x in range(1, number // 2 + 1) if number % x == 0)
 
 
pairs = {}
for i in range(2, 30001):
    sum_div = divisors(i)
    if sum_div != 1:
        if i in pairs:
            num1, num2 = i, pairs[i]
            if divisors(num1) == num2:
                print(*([num2, num1]))
        else:
            pairs[sum_div] = i
