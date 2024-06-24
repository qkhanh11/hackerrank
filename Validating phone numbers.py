import re
n = int(input())
regex_pattern = r"^[7-9]\d{9}$"
for i in range(n):
    a = bool(re.match(regex_pattern, input()))
    if a:
        print("YES")
    else:
        print("NO")