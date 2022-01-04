# Candies

for i in range(int(input())):
    val = int(input())
    j = 2
    check = True
    while check:
        if pow(2, j) - 1 == val:
            print(1)
            check = False
        elif (val % (pow(2, j) - 1)) == 0:
            print(val // ((pow(2, j) - 1)))
            check = False
        j += 1