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
        name = full_name.split()
        first_name = name[0]
        last_name = name[1]
        for mentor in self.students:
            if mentor.first_name == first_name and mentor.last_name == last_name:
                print(full_name + " was found ")
                return mentor
            else:
                print(full_name + " was not found")

    def find_mentor_by_full_name(self, full_name):
        name = full_name.split()
        first_name = name[0]
        last_name = name[1]
        for mentor in self.mentors:
            if mentor.first_name == first_name and mentor.last_name == last_name:
                print(full_name + " was found")
                return mentor
            else:
                print(full_name + " was not found")
