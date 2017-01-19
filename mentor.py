from person import Person


class Mentor(Person):

    def __init__(self, nickname, has_contract=True, salary=200000):
        super().__init__(first_name, last_name, year_of_birth, gender)
        self.nickname = nickname

    def create_by_csv(csv_path):
        students = []
        myfile = open(csv_path, "r")
        for lin in myfile:
            student.append(line)
        myfile.close()
