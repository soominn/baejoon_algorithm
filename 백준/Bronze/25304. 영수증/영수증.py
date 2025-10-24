total_price = int(input())
sum_price = 0
num = int(input())

for i in range(num):
    price, cnt = map(int, input().split())
    sum_price += price * cnt

if total_price == sum_price:
    print('Yes')
else:
    print('No')