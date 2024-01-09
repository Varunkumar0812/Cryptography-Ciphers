# Program to perform Shift Cipher - Decryption

def diff(n, f) :
    if 0 <= n - f < 26 :
        return n - f
    else :
        return 26 + (n - f)

s = input().upper()

m = max(set(s), key=s.count)
print(m)

f = abs(ord(m) - ord('E'))
print(f)

res = ""
for i in s :
    if i != ' ' :
        res += chr(ord('A') + diff(ord(i) - ord('A'), f))
    else :
        res += i
print(res)