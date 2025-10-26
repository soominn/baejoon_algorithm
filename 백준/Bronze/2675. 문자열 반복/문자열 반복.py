n = int(input())

for i in range(n):
    result = ''
    a, b = input().split()
    
    for j in range(len(b)):
        result += b[j] * int(a)
        
    print(result)