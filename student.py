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
        myfile = open(csv_path, "r")
        for line in myfile:
            line = line.lstrip().split(",")
            first_name, last_name = line[0], line[1]
            year_of_birth, gender, knowledge_level, energy_level = line[2], line[3], line[4], line[5]
            students.append(Student(first_name, last_name, year_of_birth, gender, knowledge_level, energy_level))
        myfile.close()
        return students
