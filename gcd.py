# Program to find GCD (Greatest Common Divisor) of two numbers
# This is included since gcd is required lot of times in cryptography

n1 = int(input())
n2 = int(input())

t1 = [i for i in range(1, n1) if n1 % i == 0]
t2 = [i for i in range(1, n2) if n2 % i == 0]

print("GCD : ", max(set(t1).intersection(set(t2))))

