bal = int(input())
if bal > -1:
    print(bal)
else:
    bal = str(bal)
    temp1 = int(bal[:-2] + bal[-1:])
    temp2 = int(bal[:-1])
    print(max(temp1, temp2))