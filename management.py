from person import Person
from mentor import Mentor
import random

class Management():

    @classmethod
    def fire_mentor(cls, mentor):
        mentor.has_contract = False
        return mentor.first_name + mentor.last_name + "has been fired! :("

    @classmethod
    def give_raise(cls, mentor):
        raise_percentage =  random.random()
        mentor.salary += mentor.salary * raise_percentage
        return mentor.first_name + mentor.last_name + " got a " + "{0}% raise!\n He now earns: {1:,} Ft".format(int(raise_percentage*100), int(mentor.salary))
