from person import Person


class Mentor(Person):
    def __init__(self, nickname):
        self.nickname = nickname

    def create_by_csv(csv_path):
        students = []
        myfile = open(csv_path,"r")
        for lin in myfile:
            student.append(line)
        myfile.close()
