# Triangle

temp = input().split()
val = []
for i in range(4):
    val.append(int(temp[i]))

val.sort()
while True:
    # Check for Triangle
    i, j = 0, 3
    while j > 1:
        if val[i] + val[i+1] > val[j]:
            print('TRIANGLE')
            exit(0)
        j -= 1
    j = 3
    if val[i + 1] + val[i + 2] > val[j]:
        print('TRIANGLE')
        exit(0)

    # Check for Segment
    i, j = 0, 3
    while j > 1:
        if val[i] + val[i+1] == val[j]:
            print('SEGMENT')
            exit(0)
        j -= 1
    j = 3
    if val[i + 1] + val[i + 2] == val[j]:
        print('SEGMENT')
        exit(0)

    print('IMPOSSIBLE')
    exit(0)