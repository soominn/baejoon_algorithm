N, M = map(int, input().split())
baguni = []
for i in range(N):
    baguni.append(0)

for a in range(M):
    i, j, k = map(int, input().split())

    for b in range(i, j + 1):
        baguni[b - 1] = k

print(' '.join(map(str, baguni)))