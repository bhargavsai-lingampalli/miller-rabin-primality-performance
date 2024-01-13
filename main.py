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


def return_m(num: int):
    k = 0
    while num % 2 == 0:
        k += 1
        num >>= 1

    return k, num


def miller_rabin_primality_test(num: int):
    if num % 2 == 0:
        return False if num != 2 else True

    k, m = return_m(num - 1)
    a = random.randint(2, num - 2)
    b = pow(a, m, num)

    if b == 1 or b == num - 1: return True
    for i in range(k):
        b = pow(b, 2, num)
        if b == num - 1: return True

    return False


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
