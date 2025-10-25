N, M = map(int, input().split())
baguni = []
for i in range(N):
    baguni.append(i + 1)

for a in range(M):
    i, j = map(int, input().split())
    baguni[i- 1], baguni[j - 1] = baguni[j - 1], baguni[i - 1]

print(' '.join(map(str, baguni)))