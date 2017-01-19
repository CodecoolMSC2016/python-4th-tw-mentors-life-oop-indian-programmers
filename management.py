from person import Person
from mentor import Mentor


class Management():

    @classmethod
    def fire_mentor(cls, mentor):
        mentor.has_contract = False
        return mentor.first_name + mentor.last_name + "has been fired! :("

    @classmethod
    def give_raise(cls, mentor):
        mentor.salary *= 1.05
        return mentor.first_name + mentor.last_name + " got a " + str(int(mentor.salary * 0.05)) \
            + " raise!\n He now earns: " + str(int(mentor.salary)) + "Ft"
