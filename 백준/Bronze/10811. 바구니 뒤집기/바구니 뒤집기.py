N, M = map(int, input().split())
baguni = []
for i in range(N):
    baguni.append(i + 1)

for a in range(M):
    i, j = map(int, input().split())
    
    front_val = baguni[:i - 1]
    back_val = baguni[j:]
    reverse_val = baguni[i - 1:j]
    reverse_val.reverse()

    baguni = front_val + reverse_val + back_val

print(' '.join(map(str, baguni)))