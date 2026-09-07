prime_number = []
for n in range(2, 1000):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        prime_number.append(n)
print(prime_number)
