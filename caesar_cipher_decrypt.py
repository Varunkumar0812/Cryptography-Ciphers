# Program to perform Caesar Cipher - Decryption

s = input()

t = ''.join([x for x in s if x != ' '])

res = ""

for i in t :
    t = ord(i) - ord('A') - 3
    if t < 0 :
        res += chr(ord('Z') + t)
    else :
        res += chr(ord('A') + t)

print(res)