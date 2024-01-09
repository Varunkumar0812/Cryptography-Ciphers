# Program to perform Caesar Cipher - Encryption

s = input()

t = ''.join([x for x in s.upper() if x != ' '])

res = ""

for i in t :
    res += chr(ord('A') + (ord(i) - ord('A') + 3) % 26)

print(res)