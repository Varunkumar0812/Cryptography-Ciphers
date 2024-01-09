# Program to perform Shift Cipher - Encryption

s = input().upper()
k = int(input())

t = ''.join([x for x in s if x != ' '])

res = ''

for i in t :
    res += chr(ord('A') + (ord('A') - ord(i) + k) % 26)

print(res)