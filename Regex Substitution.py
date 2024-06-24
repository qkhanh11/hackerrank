import re
k = int(input())
s = input()

for i in range(k-1):
    s += '\n'
    s = s + input()


s1 = re.sub(r'(?<= )&&(?= )', 'and', s)
print(re.sub(r'(?<= )\|\|(?= )', 'or', s1))