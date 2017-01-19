from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from laptop import Laptop
from pub import Pub
from management import Management
from mentor_room import Mentor_Room
import os
import time
import random


def main():
    cc_msc = CodecoolClass.create_local()
    mentor = random.choice(cc_msc.mentors)
    print("It's 8 am in the morning, our hero, " + mentor.first_name + " starts his daily routine in the Pub.")
    time.sleep(1)
    pub = Pub("Paprika")
    print("Location: " + pub.name + " Pub")
    for key, value in vars(pub).items():
        time.sleep(0.3)
        print("\t" + key + ": " + str(value))
    print("How many rounds you wish to drink?")
    number_of_rounds = int(input("\n"))
    for i in range(number_of_rounds):
        print("Serving alcohol to people...\n" + pub.serve_alcohol())
        print(pub.change_music())
        time.sleep(0.6)
    print("After so many rounds a bar fight starts,the security comes to handle it")
    print(pub.handle_pub_fight())
    time.sleep(1)
    print("It's 9AM our hero mentor,has arrived to CodeCool,As soon as he arrives the management calls him")
    time.sleep(1)
    print("Management:Dear mentor for your hard and soulful work attitude we have decided to give you a rasise in your salary")
    time.sleep(1)
    print(Management.give_raise(mentor))


if __name__ == '__main__':
    main()
