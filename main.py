import random
import matplotlib.pyplot as plt
import timeit


def normal_prime_test(num: int):
    if num % 2 == 0:
        return False if num != 2 else True

    for i in range(3, int(num ** .5) + 1, 2):
        if num % i == 0:
            return False

    return True


def single_test(a, n, m):
    if pow(a, m, n) == 1:
        return True

    while m < n - 1:
        if pow(a, m, n) == n - 1:
            return True
        m <<= 1

    return False


def miller_rabin_primality_test(num, k=40):
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 2 == 0:
        return False

    m = num - 1
    while m % 2 == 0:
        m >>= 1

    for _ in range(k):
        a = random.randint(2, num - 2)
        if not single_test(a, num, m):
            return False

    return True


mr_times = timeit.repeat(lambda: miller_rabin_primality_test(random.randrange(3, 10000000000000000, 2)), repeat=100,
                         number=10)
normal_times = timeit.repeat(lambda: normal_prime_test(random.randrange(3, 10000000000000000, 2)), repeat=100,
                             number=10)

plt.title('Miller Rabin Primality vs Normal Prime Test')
plt.xlabel('No of Times')
plt.ylabel('Time Taken')

plt.plot(normal_times, 'r', label='Normal Function')
plt.plot(mr_times, 'g', label='Miller Rabin Primality Function')

plt.legend()
plt.show()
