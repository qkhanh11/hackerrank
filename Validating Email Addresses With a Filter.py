def fun(s):
    try:
        username, url = s.split('@')                                           
        website, extension = url.split('.')
    except ValueError:
        return False

    if username.replace('-', '').replace('_', '').isalnum() is False:       # thay xóa ký tự -, _ (thay thế '-' và '_' thành '' bằng hàm replace)
        return False
    elif website.isalnum() is False:                                        #kiểm tra phần website có phải là chuỗi chữ và số không
        return False
    elif len(extension) > 3:
        return False
    elif extension.isalpha() is False:                                      #kiểm tra phần extension có phải là chuỗi chữ không
        return False
    else:
        return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)