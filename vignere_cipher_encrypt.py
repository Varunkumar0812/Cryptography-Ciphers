# Program to perform Vignere Cipher - Encryption

s = input()

t = ''.join([x for x in s if x != ' '])

keyword = input()

def let_val(x) :
    return ord(x) - ord('A')

res = ''

for i in range(0, len(t), len(keyword)) :
    g = 0
    for j in t[i:i + len(keyword)] :
        res += chr(ord('A') + (let_val(j) + let_val(keyword[g])) % 26)
        g += 1
    res += ' '
print(res)