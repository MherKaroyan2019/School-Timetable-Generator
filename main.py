class Student:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects


class Subject:
    def __init__(self, name, weekNumber):
        self.name = name


class Teacher:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects


class Classroom:
    def __init__(self, name, capacity, room_type):
        self.name = name
        self.capacity = capacity
        self.room_type = room_type

mathAA = Subject("Math AA", 2)
physics = Subject("Physics", 2)
cs = Subject("Computer Science", 2)
english = Subject("English B", 2)

student1 = Student("Hollow", [mathAA, physics, cs])
student2 = Student("Apple", [english, physics, cs])
student3 = Student("Yellow", [mathAA, english, cs])

teacher1 = Teacher("Spider", [mathAA, physics])
teacher2 = Teacher("Computer", [cs])
teacher3 = Teacher("Common", [english])

classroom1 = Classroom("1", 2, "projector")
classroom2 = Classroom("2", 2, "normal")

days = 3
classesPerDay = 3