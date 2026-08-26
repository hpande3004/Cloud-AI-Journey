'''Mini Project 3
Employee Management System'''

class Employee:

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ₹{self.salary}")

    def calculate_bonus(self):
        return self.salary * 0.10


class Developer(Employee):

    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print(f"Programming Language: {self.programming_language}")

    def calculate_bonus(self):
        return self.salary * 0.15


class Manager(Employee):

    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    def display_details(self):
        super().display_details()
        print(f"Team Size: {self.team_size}")

    def calculate_bonus(self):
        return self.salary * 0.20


developer = Developer(
    "Rahul",
    "DEV101",
    60000,
    "Python"
)

manager = Manager(
    "Priya",
    "MGR101",
    90000,
    8
)


print("===== Developer =====")

developer.display_details()

print(f"Bonus: ₹{developer.calculate_bonus()}")


print("\n===== Manager =====")

manager.display_details()

print(f"Bonus: ₹{manager.calculate_bonus()}")