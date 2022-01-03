# Anto and danik

a = d = 0
_ = input()
val = input()
for i in val:
    if i == 'A':
        a += 1
    else:
        d += 1

if a > d:
    print('Anton')
elif d > a:
    print('Danik')
else:
    print('Friendship')