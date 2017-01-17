from person import Person


class Student(Person):

    def __init__(self, knowledge_level, energy_level):
        self.knowledge_level = knowledge_level
        self.energy_level = energy_level

    def create_by_csv(csv_path):
        my_file = open(csv_path, "r")
        students = []
        for line in my_file:
            students.append(line)
        my_file.close()
