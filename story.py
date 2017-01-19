from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from laptop import Laptop
from pub import Pub
from management import Management
from mentor_room import Mentor_Room
import os
import time


def start_story(filename):
    with open(filename) as f:
        for line in f:
            print(line)
            time.sleep(0.5)


def main():
    start_story("story.txt")
    time.sleep(1)
    pub = Pub("Paprika")
    print("Location: " + pub.name + " Pub")
    for key, value in vars(pub).items():
        time.sleep(0.3)
        print("\t" + key + ": " + str(value))
    print("How many rounds you wish to drink?")
    number_of_rounds=int(input("\n"))
    for i in range(number_of_rounds):
        print("Serving alcohol to people...\n" + pub.serve_alcohol())
        print(pub.change_music())
        time.sleep(0.6)
    print("After so many rounds a bar fight starts,the security comes to handle it")
    print(pub.handle_pub_fight())


if __name__ == '__main__':
    main()
