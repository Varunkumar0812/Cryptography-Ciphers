# Program to perform Affine Cipher - Decryption

s = 'QAOOYQQEVHEQV'
a = 15
k = 16

t = ''.join([x for x in s if x != ' '])

res = ''

for i in t :
    for j in range(26) :
        if (a*j + k) % 26 == ord(i) - ord('A') :
            break
    res += chr(ord('A') + j)

print(res)