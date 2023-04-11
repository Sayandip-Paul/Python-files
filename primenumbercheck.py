def prime_no(num):
    if n <= 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return True
    return False

n = 23
if prime_no(n):
    print(n,"is prime")
else:
    print(n,"is not prime")



