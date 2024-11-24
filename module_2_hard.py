def x_password(number):
    password = ''
    a = 1
    while a < number:
        b = 2
        while b < number:
            if b <= a:
                b += 1
                continue
            if number % (a + b) == 0:
                password += str(a) + str(b)
            b += 1
        a += 1
    return password

i = 3
while i < 21:
    result = x_password(i)
    print(f"{i} - {result}")
    i += 1


def x_password(number):
    password = ''
    for a in range(1, number):
        for b in range(2, number):
            if b <= a:
                continue
            if number % (a + b) == 0:
                password += str(a) + str(b)
    return password
for i in range(3, 21):
    result = x_password(i)
    print(f"{i} - {result}")
