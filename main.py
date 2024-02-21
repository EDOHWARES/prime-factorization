def factors_s():
    """
    :return: a list of prime factors of a value inputted by a user
    """

    n = 0

    factors = []
    primefactors = []

    while n < 2:
        try:
            n = int(input("Enter a number to print it prime factors: "))
        except ValueError:
            print("Input must be a valid digit!")

        if n < 2:
            print("Input must be greater than 2")
        else:
            pass

    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    return factors


def check_if_prime(n):
    li = []
    if n < 2:
        return False
    else:
        for i in range(1, n+1):
            if n % i == 0:
                li.append(i)

    if len(li) == 2:
        return True
    else:
        return False


def prime_numbers():
    prime = []
    factors = factors_s()
    for num in factors:
        if check_if_prime(num):
            prime.append(num)
        else:
            pass

    return prime


if __name__ == "__main__":
    print(prime_numbers())










