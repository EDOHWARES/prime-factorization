def prime_factors(factors):
    prime = []
    for el in factors:
        for i in range(2, el+1):
            k = []
            if el % i == 0:
                k.append(i)
    prime.append(k)

    return prime


k = [3, 4, 5, 6, 7, 8, 9, 10]

print(prime_factors(k))



