from datetime import datetime

person1 = ["Іванчук Іван Іванович", "01.01.1980"]
person2 = ["Петренко Петро Петрович", "15.05.1995"]
person3 = ["Сидораанен Сидір Сидорович", "30.11.1988"]

people_tuple = (person1, person2, person3)


def sort_by_birthdate(people_tuple):
    for i in range(len(people_tuple)):
        date_obj = datetime.strptime(people_tuple[i][1], "%d.%m.%Y")
        start_date = datetime(1970, 1, 1)
        date_to_days = (date_obj - start_date).days
        people_tuple[i].append(date_to_days)

    new = tuple(sorted(people_tuple, key=lambda x: x[2]))

    for j in range(len(people_tuple)):
        people_tuple[j].remove(people_tuple[j][2])

    print(new)


sort_by_birthdate(people_tuple)
