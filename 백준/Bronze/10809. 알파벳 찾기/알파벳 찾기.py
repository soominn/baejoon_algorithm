s = input()
alpha_li = [-1] * 26

for i in range(len(s)):
    if alpha_li[ord(s[i]) - 97] == -1:
        alpha_li[ord(s[i]) - 97] = i

print(*alpha_li)