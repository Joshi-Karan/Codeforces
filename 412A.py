# Poster
val = input().split()
n = int(val[0])
k = int(val[1])
slogan = input()

if k == n == 1:
    print('PRINT', slogan)
elif k == 1:
    for i in range(len(slogan) - 1):
        print('PRINT', slogan[i])
        print('RIGHT')
    print('PRINT', slogan[i + 1])
elif k == n:
    for i in range(len(slogan) - 1, 0, -1):
        print('PRINT', slogan[i])
        print('LEFT')
    print('PRINT', slogan[0])
else:
    if k >= (n // 2 + 1):
        while k != n:
            print('RIGHT')
            k += 1
        for i in range(len(slogan) - 1, 0, -1):
            print('PRINT', slogan[i])
            print('LEFT')
        print('PRINT', slogan[0])
    else:
        while k != 1:
            print('LEFT')
            k -= 1
        for i in range(len(slogan) - 1):
            print('PRINT', slogan[i])
            print('RIGHT')
        print('PRINT', slogan[i + 1])