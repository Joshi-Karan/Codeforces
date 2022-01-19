val = input()
if len(val) < 7:
    print('NO')
    exit(0)

one = 0
zero = 0
prev = val[0]
if val[0] == '1':
    one = 1
else:
    zero = 1

for i in val[1:]:
    if one == 7 or zero == 7:
        print('YES')
        exit(0)
    if i == prev:
        if i == '1':
            one += 1
        else:
            zero += 1
    else:
        prev = i
        if prev == "1":
            one = 1
            zero = 0
        else:
            zero = 1
            one = 0
if one == 7 or zero == 7:
    print('YES')
else:
    print('NO')
