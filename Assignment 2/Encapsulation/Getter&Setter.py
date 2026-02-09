class Student:
    def __init__(self):
        self.__marks = 0

    def setMarks(self, m):
        self.__marks = m

    def getMarks(self):
        return self.__marks

s = Student()
s.setMarks(85)
print("Marks:", s.getMarks())
