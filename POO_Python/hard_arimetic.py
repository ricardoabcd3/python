'''import time
def factorial(n):
    answer= 1

    while n > 1:
        answer *=n
        n -=1
    return answer
def factorial_r(n):
    if n == 1:
        return 1
    return n * factorial(n* -1)
if __name__=="__main__":
    n =int(input("you know "))
    begin= time.time()
    print(factorial(n))
    final = time.time()
    print(final - begin)
    begin= time.time()
    print(factorial_r(n))
    final = time.time()
    print(final - begin)
'''
import time

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta


def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


if __name__ == '__main__':
    n = 200000

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)