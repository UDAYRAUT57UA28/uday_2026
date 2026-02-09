class Student:
    def __init__(self, name, marks):
        self.name = name        # public
        self.__marks = marks    # private

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.__marks)

s = Student("Uday", 90)
s.display()
