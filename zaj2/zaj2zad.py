# 1.
k = [8, 0, 17, 1, 10, 13, 13, 13, 10, 3, 1, 1, 13, 13]
print(k)

for i in range(len(k)):
    if 13 in k:
        k.remove(13)
    else:
        break

print(k)

# 2.
k = [8, 0, 17, 1, 10, 13, 19, 13, 10, 3, 1, 1]
while 1 in k:
    k.remove(1)

print(k)

# 3.
k = [8, 0, 17, 1, 10, 13, 19, 13, 10, 3, 1, 1]
for i in range(1, len(k), 2):
    print(k[i], end=' ')
print("")

# 4.
print(k)
k = k[1::2]
print(k)

# 5.
k = [8, 0, 17, 1, 10, 13, 19, 13, 10, 3, 1, 1]
for i in range(0, len(k), 2):
    print(k[-i - 1], end=' ')
print("")

# 6.
k = k[::-2]
print("6:", k)

# 7.
k = [8, 0, 17, 1, 10, 13, 19, 13, 10, 3, 1, 1]
l = [(i, k[i]) for i in range(len(k))]
print(l)

# 8.
l.sort(key=lambda x: x[1])
print(l)

# 9.
k = [8, 0, 17, 1, 10, 13, 19, 13, 10, 3, 1, 1]
l = [(i, k[i]) for i in range(len(k)) if k[i] % 2 == 0]
print(l)

# 10.
l = [(i, k[i]) if i < k[i] else (k[i], i) for i in range(len(k))]
print(l)

# 11.
k = [[1 if 3 < i < 8 and 3 < j < 8 else 0 for j in range(12)] for i in range(12)]
for i in range(12):
    print(k[i])

print("")
k = [[1 if (i == j) or (i == 11 - j) else 0 for j in range(12)] for i in range(12)]
for i in range(12):
    print(k[i])

print("")
k = [[1 if (j + i % 2) % 2 == 0 else 0 for j in range(12)] for i in range(12)]
for i in range(12):
    print(k[i])
