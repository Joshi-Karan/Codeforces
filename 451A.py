# Playing with sticks
val = input().split()
m, n = int(val[0]), int(val[1])
if min(m, n)%2 == 0:
    print('Malvika')
else:
    print('Akshat')