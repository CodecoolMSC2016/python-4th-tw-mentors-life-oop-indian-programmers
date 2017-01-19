from person import Person
import csv


class Student(Person):

    def __init__(self, first_name, last_name, year_of_birth, gender, knowledge_level, energy_level):
        super().__init__(first_name, last_name, year_of_birth, gender)
        self.knowledge_level = knowledge_level
        self.energy_level = energy_level

    @classmethod
    def create_by_csv(cls, csv_path):
        students = []
        with open(csv_path, "r") as csvfile:
            csv_file = csv.reader(csvfile)
            for row in csv_file:
                student = Student(row[0], row[1])
                students.append(student)
        return students
