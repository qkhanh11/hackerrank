cube = lambda x: x**3

def fibonacci(n):
    list1 = []
    list1.append(0)
    list1.append(1)
    for i in range(2,n,1):
        list1.append(list1[i-1] + list1[i-2])
    return list1

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))