class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Rakesh", 25)
s2 = Student("Amit", 22)
s3 = Student("Neha", 21)

s1.show_details()
s2.show_details()
s3.show_details()
