import re
S = input()
k= input()
matches = list(re.finditer(f'(?={k})', S))
if not matches:
    print((-1, -1))
else:
    for match in matches:
        start_index = match.start()
        end_index = start_index + len(k) - 1
        print((start_index, end_index))