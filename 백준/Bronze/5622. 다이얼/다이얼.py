dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
count = 0
word = input()

for w in word:
    for i, v in enumerate(dial):
        if v.find(w) != -1:
            count += i + 3

print(count)