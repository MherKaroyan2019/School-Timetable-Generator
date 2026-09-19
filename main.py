class Student:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects


class Subject:
    def __init__(self, name, level):
        self.name = name
        self.level = level


class Teacher:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects


class Classroom:
    def __init__(self, name, capacity, room_type):
        self.name = name
        self.capacity = capacity
        self.room_type = room_type