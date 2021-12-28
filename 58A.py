# Chat Room
s = input()
word = ['h','e','l','l','o']
clear = False
for i in range(len(s)):
    if s[i] == word[0]:
        word.remove(s[i])
    if word == []:
        clear = True
        break
if clear:
    print('YES')
else:
    print("NO")