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

def read_story_from_file(filename):
    story_list = []
    with open(filename) as f:
        for line in f:
            story_list.append(line)
    return story_list

def generate_story(story_list):
    index = 0
    while index < len(story_list):
        time.sleep(0.5)
        yield story_list[index] 
        index += 1


def main():
    cc_msc = CodecoolClass.create_local()
    mentor = random.choice(cc_msc.mentors)
    mentor_room = Mentor_Room()
    bfa_student = random.choice(cc_msc.students)
    pub = Pub("Paprika Pub")
    story_list = read_story_from_file("story.txt")
    story = generate_story(story_list)
    print(next(story) + mentor.last_name + " " + mentor.first_name, end='')
    print(next(story), end='')
    input()
    print(next(story) + " " +pub.name)
    for key, value in vars(pub).items():
        time.sleep(0.3)
        print("\t" + key + ": " + str(value))
    print(next(story))
    number_of_rounds = int(input(""))
    alcohol_serving_str = next(story)
    for i in range(number_of_rounds):
        print( alcohol_serving_str + pub.serve_alcohol())
        time.sleep(1)
        print(pub.change_music())
        time.sleep(1)
    print(next(story))
    print(pub.handle_pub_fight())
    for counter in range(2):
        time.sleep(1)
        print(next(story))
    print(Management.give_raise(mentor))
    input()
    
    print(next(story))
    print(mentor_room.start_bfa())
    time.sleep(0.5)
    print(bfa_student.last_name + bfa_student.first_name + next(story))
    time.sleep(1)
    print(bfa_student.last_name + next(story))
    laptop = Laptop()
    for msg in laptop.turn_on():
        #os.system("clear")
        print(msg)
    for msg in laptop.run_code():
        print(msg)
    print(next(story) +
          bfa_student.last_name + bfa_student.first_name + ".")
    print(mentor_room.gets_dirty())
    print(mentor_room.stop_bfa())
    print(mentor_room.open_window())
    time.sleep(1)
    print(next(story) +
          mentor.first_name + mentor.last_name + ".")
    print(Management.fire_mentor(mentor))
    print(mentor.first_name + mentor.last_name + next(story))

if __name__ == '__main__':
    main()
