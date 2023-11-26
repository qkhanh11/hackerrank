def is_not_palindromic(n):
    str_number = str(n)
    return str_number != str_number[::-1]


def is_not_positive(n):
    return n<0

def run():
    input()
    n = [int(i) for i in input().split()]
    if all([is_not_positive(i) for i in n]):
        print("False")
        return 
    if all([is_not_palindromic(i) for i in n]):
        print("False")
        return 
    print("True")

run()