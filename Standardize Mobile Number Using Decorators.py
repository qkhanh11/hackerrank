

def wrapper(f):
    def fun(l):
        k=[]
        for i in l:
            if len(i) == 11:
               if i[0] != '0':
                continue
               k.append(i[1:])
            if len(i) == 12:
               if i[0:2] != '91':
                   continue
               k.append(i[2:])
            if len(i) == 10:
               k.append(i)
            if len(i) == 13:
               if i[0] not in ['+','.']:
                  continue
               if i[1:3] != '91':
                  continue
               k.append(i[3:])
        for i in range(len(k)):
           k[i] = '+91' +' '+ k[i][0:5]+' '+k[i][5:]

        return f(k)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 