'''Class Method'''
class Student:
    school = "ABC School"
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
Student.change_school("XYZ School")
print(Student.school)                        # Output: XYZ School

class Employee:
    company = "Wipro"
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
Employee.change_company("Microsoft")
print(Employee.company)                      # Output: Microsoft
