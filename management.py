from person import Person
from mentor import Mentor


class Management(Person):
    def __init__(self):
        super().__init__()

    def fire_mentor(self,name):
        if isinstance(name,Mentor):
            super.has_contract = False

    def give_raise(self,name,amount):
        if isinstance(name,Mentor):
            super().salary += amount
