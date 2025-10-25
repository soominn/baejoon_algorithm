num_li = []
for i in range(9):
    num = int(input())
    num_li.append(num)

max_num = max(num_li)
max_index = num_li.index(max_num)

print(max_num)
print(max_index + 1)