# Dragon

temp = input().split()
s, n = int(temp[0]), int(temp[1])
a = []
for _ in range(n):
    val = input().split()
    a.append([int(val[0]), int(val[1])])
for x, y in sorted(a):
    if s > x:
        s += y
    else:
        print('NO')
        exit(0)
print('YES')
