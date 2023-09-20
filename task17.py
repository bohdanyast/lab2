class Student:
    def __init__(self, name, courses, phone_number, email, degree, city):
        self.name = name
        self.courses = courses
        self.phone_number = phone_number
        self.email = email
        self.degree = degree
        self.city = city

        print("Створено об’єкт для "+ name)

    def printDetails(self):
        # Виводить атрибути
        print("Ім’я: ", self.name)
        print("Курси: ", self.courses)
        print("Телефон: ", self.phone_number)
        print("Пошта: ", self.email)
        print("Курс: ", self.degree)
        print("Місто: ", self.city)


    def enroll(self, course):
        # Додає навчальні курси
        self.courses.append(course)


student1 = Student("Mary", ["L548"], 3432442, 'dfkjndgkdjf@gmail.com',
                   2, 'Kyiv')


newcourse = input("Уведіть номер курсу або 'stop' ")
while newcourse != "stop":
    student1.enroll(newcourse)
    print("Уведіть курси, які вивчає", student1.name)
    newcourse = input("Уведіть номер курсу або 'stop' ")

student1.printDetails()