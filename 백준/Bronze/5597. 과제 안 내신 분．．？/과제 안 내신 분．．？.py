num_li = [n + 1 for n in range(30)]

for i in range(28):
    num = int(input())
    num_li.remove(num)

print(min(num_li))
print(max(num_li))