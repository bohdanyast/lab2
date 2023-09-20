import random


def random_array(N):
    arr = []
    while len(arr) < N:
        num = random.randint(1, N)
        if arr.count(num) == 0:
            arr.append(num)

    print(arr)


random_array(23)
