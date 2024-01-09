# Program to find the prime numbers
# This is included since gcd is required lot of times in cryptography

def is_prime(n) :
    f = 0
    for i in range(2, int(n / 2)) :
        if n % i == 0 :
            f += 1
    if f > 0 or n == 4 :
        return False
    else :
        return True
    
n = int(input())

t = [i for i in range(1, n + 1) if n % i == 0 and is_prime(i)]
print(t)