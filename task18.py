class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary_percent(self, percentage):
        self.salary = round(self.salary + (1 / percentage) * self.salary)

    def increase_age_by_1(self):
        self.age += 1

    def update_position(self, new_position):
        self.position = new_position

    def print_details(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Position: {self.position}')
        print(f'Salary: {self.salary}')


employee = Employee('Sanya Cegla', 24, 'builder', 500)
employee.increase_age_by_1()
employee.update_position('main builder')
employee.increase_salary_percent(20)
employee.print_details()
