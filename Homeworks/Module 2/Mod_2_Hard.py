def ancient_cipher(n):
    result = ''
    for i in range(1, n):
        for j in range(i, n):
            if n % (i + j) == 0 and not i == j:
                result += f'{i}{j}'
    return result


num = int(input("Enter num (between 3 and 20): "))
if 3 <= num <= 20:
    password = ancient_cipher(num)
    print("Pass: ", password)
else:
    print("The num should be in range of 3 to 20")
