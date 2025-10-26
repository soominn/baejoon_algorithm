a, b = map(reversed, input().split())
a, b = int(''.join(list(a))), int(''.join(list(b)))

print(a) if a > b else print(b)