# Multiply by 2, divide by 6

for i in range(int(input())):
    val = int(input())
    moves = move3 = move2 = 0
    temp = val
    while temp % 3 == 0:
        move3 += 1
        temp = temp // 3
    temp = val
    while temp % 2 == 0:
        move2 += 1
        temp = temp // 2
    if val == 1:
        print(0)
    elif move2 == move3 == 0:
        print(-1)
    elif move2 > move3:
        print(-1)
    else:
        moves = move3 + (move3 - move2)
        val = val * (pow(2, move3-move2))
        check = True
        while val > 1:
            val /= 6
            if val.is_integer() == False:
                check = False
                break
        if check:
            print(moves)
        else:
            print(-1)