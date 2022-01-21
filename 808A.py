# Lucky Year

curr = input()
size = len(curr)
curr = int(curr)
if curr < 10:
    print(1)
elif curr % (10**(size - 1)) == 0:
    print(10**(size - 1))
else:
    print((10**(size - 1)) - (curr % (10**(size - 1))))