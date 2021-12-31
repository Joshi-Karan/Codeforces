# Taxi [or Fake-Taxi Idk ;) ]

one = two = three = four = taxi = 0
_ = input()
val = input().split()
for i in range(len(val)):
    if val[i] == '1':
        one += 1
    elif val[i] == '2':
        two += 1
    elif val[i] == '3':
        three += 1
    elif val[i] == '4':
        four += 1

taxi = four + three + two // 2
one -= three
if two % 2 == 1:
    taxi += 1
    one -= 2

if one > 0:
    taxi += (one + 3)//4

print(taxi)