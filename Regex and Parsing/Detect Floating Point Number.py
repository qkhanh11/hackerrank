for _ in range(int(input())):
    str1 = input()
    str2=str1.replace('+', '').replace('-', '').replace('.', '',1)
    try:
        int(str2)
    except:
        print(False)
        continue
    n = str1.find('+')
    if n!=0 and n != -1:
        print(False)
        continue
    n = str1.find('-')
    if n!=0 and n != -1:
        print(False)
        continue
    n = str1.find('.')
    if n==len(str1)-1 or n == -1:
        print(False)
        continue
    print(True)

