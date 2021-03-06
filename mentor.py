from person import Person
import random


class Mentor(Person):

    def __init__(self, first_name, last_name, year_of_birth, gender, nickname, has_contract=True):
        super().__init__(first_name, last_name, year_of_birth, gender)
        self.nickname = nickname
        self.salary = random.randint(0, 1000000)

    @classmethod
    def create_by_csv(cls, csv_path):
        mentors = []
        myfile = open("mentors.csv", "r")
        for line in myfile:
            line = line.split(",")
            first_name, last_name = line[0], line[1]
            year_of_birth, gender, nickname = line[2], line[3], line[4]
            mentors.append(Mentor(first_name, last_name, year_of_birth, gender, nickname))
        myfile.close()
        return mentors
