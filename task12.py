array = [4, 54, 5, 35, 3, 5, 4, 6, 4, 3, 6, 3, 36, 4, 345, 34, 5, 34, 2, 5]
array_repeated_ints = []
array_indexes = []

for i in range(len(array)):
    if array.count(array[i]) >= 2 and array_repeated_ints.count(array[i]) == 0:
        array_repeated_ints.append(array[i])
        array_indexes.append(array.index(array[i])+1)

for k in range(len(array_repeated_ints)):
    print(f'{array_indexes[k]} — {array_repeated_ints[k]}')











