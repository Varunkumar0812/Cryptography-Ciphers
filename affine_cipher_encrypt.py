# Program to perform Affine Cipher - Encryption

s = input()
a = int(input())
k = int(input())

t = ''.join([x for x in s if x != ' '])

res = ''

for i in t :
    res += chr(ord('A') + ((a*(ord(i) - ord('A')) + k) % 26))

print(res)