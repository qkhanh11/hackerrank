def is_palindromic(n):
    str_number = str(n)
    return str_number == str_number[::-1]


def is_not_positive(n):
    return n<0

def run():
    input()
    n = [int(i) for i in input().split()]
    if any([is_not_positive(i) for i in n]):
        print("False")
        return 
    if any([is_palindromic(i) for i in n]):
        print("True")
        return 
    print("False")

run()

