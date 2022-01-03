# Bear and Three Balls

_ = input()
val = input().split()
for i in range (len(val)):
    val[i] = int(val[i])
val.sort()

val = set(val)
val = list(val)
check = False
if len(val) >= 3:
    for i in range(0, len(val) - 2):
        if (val[i + 2] - val[i]) <= 2:
            check = True
            break

if check:
    print("YES")
else:
    print("NO")