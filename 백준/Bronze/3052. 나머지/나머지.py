num_li = []
for i in range(10):
    num = int(input()) % 42
    num_li.append(num)

num_set = set(num_li)
print(len(num_set))