from person import Person
import csv


class Student(Person):

    def __init__(self, knowledge_level, energy_level):
        self.knowledge_level = knowledge_level
        self.energy_level = energy_level

    def create_by_csv(csv_path):
        students = []
        with open(csv_path, "r") as csvfile:
            csv_file = csv.reader(csvfile)
            for row in csv_file:
                student = Student(row[0], row[1])
                students.append(student)
