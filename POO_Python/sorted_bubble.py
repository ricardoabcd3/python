import random


def sorted_bubble(list):
    n = len(list)

    for i in range(n):
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)

            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list

if __name__ == '__main__':
    try:

        size_list = int(input('how long is the list? '))
    except ValueError:
        print('wrong value')

    list = [random.randint(0, 100)*-1 for i in range(size_list)]
    print(list)

    sorted_list = sorted_bubble(list)
    print(sorted_list)