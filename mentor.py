from person import Person


class Mentor(Person):

    def __init__(self, first_name, last_name, year_of_birth, gender, nickname, has_contract=True, salary=200000):
        super().__init__(first_name, last_name, year_of_birth, gender)
        self.nickname = nickname

    @classmethod
    def create_by_csv(cls, csv_path):
        mentors = []
        myfile = open(csv_path, "r")
        for line in myfile:
            first_name, last_name = line[0], line[1]
            year_of_birth, gender, nickname = line[2], line[3], line[4]
            mentors.append(Mentor(first_name, last_name, year_of_birth, gender, nickname))
        myfile.close()
        return mentors
