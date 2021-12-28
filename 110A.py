# Nearly Lucky Number

val = input()
luck = 0
for i in range(len(val)):
    if int(val[i]) in (4, 7):
        luck += 1

if luck in (4, 7):
    print('YES')
else:
    print('NO')