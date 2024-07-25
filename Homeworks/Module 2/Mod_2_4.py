numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
neutral_shit_breaking_my_code = []

for i in numbers:
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if i == 1:
        neutral_shit_breaking_my_code.append(i)
    elif is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print('Primes: ', primes)
print('Composites: ', not_primes)
print('Neutral: ', neutral_shit_breaking_my_code)
