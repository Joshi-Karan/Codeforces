# Square

for _ in range(int(input())):
    sq1 = input().split()
    sq2 = input().split()
    for i in range(2):
        sq1[i] = int(sq1[i])
    for i in range(2):
        sq2[i] = int(sq2[i])
    
    sq1.sort()
    sq2.sort()
    if sq1[0] + sq2[0] == sq1[1] and sq1[0] + sq2[0] == sq2[1]:
        print('Yes')
    else:
        print('No')