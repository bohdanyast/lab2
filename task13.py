list_1 = ['qwerty', 'relax', 'mirniy', 'clown', 'iathebest', 'det']
list_2 = ['chess', 'relax', 'garticphone', 'iathebest', 'det']


def only_in_first(arr1, arr2):
    arr = []

    for word in list_1:
        if word not in list_2:
            arr.append(word)

    print(arr)


def only_in_second(arr1, arr2):
    arr = []

    for word in list_2:
        if word not in list_1:
            arr.append(word)

    print(arr)


only_in_first(list_1, list_2)
only_in_second(list_1, list_2)
