from mentor import Mentor
from student import Student


class CodecoolClass:

    def __init__(self, location, year, mentors, students):
        self.locaton = location
        self.year = year
        self.mentors = mentors
        self.students = students

    @classmethod
    def create_local(cls):
        return CodecoolClass("Miskolc", 2016, Mentor.create_by_csv("mentors.csv"), Student.create_by_csv("students.csv"))

    def find_student_by_full_name(self, full_name):
        name = full_name.strip(" ")
        for student in self.students:
            if (student.first_name + student.last_name).strip(" ") == name:
                print(name + " was found ")
                return student
        else:
            print(name + " was not found")

    def find_mentor_by_full_name(self, full_name):
        name = full_name.strip(" ")
        for mentor in self.mentors:
            if (mentor.first_name + mentor.last_name).strip(" ") == name:
                print(name + " was found ")
                return mentor
        else:
            print(name + " was not found")
