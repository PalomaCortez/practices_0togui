## C10 Inheritance and Polymorphism

class Student:
    total_students = 0

    def __init__(self, first, last, email, phone):
        self.first = first
        self.last = last
        self.email = email
        self.phone = phone
        Student.total_students += 1

    def print_full_name(self):
        print(self.first + " " + self.last)

    def change_phone(self):
        self.phone = new_phone


class GradStudent(Student):
    total_grad_students = 0

    def __init__(self, first, last, email, phone, degree):
        super().__init__(first, last, email, phone)
        self.degree = degree
        GradStudent.total_grad_students += 1

    def print_deg_info(self):
        print("{} in pursuing {} degree".format(self.first, self.degree))


s1 = Student('John', 'Doe', 'john.doe@email.com', 1243645)
s2 = Student('Jack', 'Stiller', 'jack.doe@email.com', 3687987)
gs1 = GradStudent('Mike', 'Scott', 'mike.scott@email.com', 8796666, 'PHD')

gs1.print_full_name()
gs1.print_deg_info()
print(gs1.total_grad_students)
print(gs1.total_students)


class Employee:
    def __init__(self, f_name, l_name, address, age):
        self.f_name = f_name
        self.l_name = l_name
        self.address = address
        self.age = age

    def print_full_name(self):
        print("Employee full name is {} {}".format(self.f_name, self.l_name))


emp1 = Employee('Steve', 'Johnson', 'Main St', 30)

lst = [emp1, s1, gs1]
for i in lst:
    i.print_full_name()
    
