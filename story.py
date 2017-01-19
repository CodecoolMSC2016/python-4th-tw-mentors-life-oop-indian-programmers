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

def generate_story_text(story_list):
    index = 0
    while index < len(story_list):
        time.sleep(0.5)
        yield story_list[index] 
        index += 1

def test_int_input():
    while True:
        usr_input = input()
        if usr_input.isnumeric():
            return int(usr_input)
        

def play_pub_scene(story, mentor, pub):
    print(next(story) + mentor.last_name + " " + mentor.first_name, end='')
    print(next(story))
    time.sleep(0.5)
    print(next(story) + " " +pub.name)
    for key, value in vars(pub).items():
        time.sleep(0.3)
        print("\t" + key + ": " + str(value))
    print(pub.change_music())
    print("\n" + next(story))
    number_of_rounds = test_int_input()
    next(story)
    for i in range(number_of_rounds):
        print(pub.serve_alcohol())
        time.sleep(1)
    print(pub.calc_chance_for_fight() + "\n")
    print(next(story), end="")
    print(pub.handle_pub_fight() + "\n")

def play_management_scene(story, mentor):
    for counter in range(2):
        print(next(story))
        time.sleep(1.5)
    print(Management.give_raise(mentor) + "\n")
    time.sleep(1)
    print(next(story))

def play_BFA_scene(story, mentor, mentor_room, bfa_student, laptop):
    print(mentor_room.start_bfa())
    time.sleep(0.5)
    print(bfa_student.last_name + " " + bfa_student.first_name + next(story))
    time.sleep(1)
    print(bfa_student.last_name + next(story))
    time.sleep(2)
    for msg in laptop.turn_on():
        os.system("clear")
        print(msg)
        time.sleep(0.1)
    time.sleep(1)
    for msg in laptop.run_code():
        time.sleep(0.3)
        print(msg)
    time.sleep(2)
    for msg in laptop.turn_off():
        os.system("clear")
        print(msg)
        time.sleep(0.1)


def play_ending_scene(story, mentor, mentor_room, bfa_student):
    print("\n" + next(story) +
          bfa_student.last_name + bfa_student.first_name + ".")
    print(mentor_room.gets_dirty())
    print("\n" + mentor_room.stop_bfa() + "\n")
    time.sleep(0.5)
    print(mentor_room.open_window())
    time.sleep(1)
    print(next(story) +
          mentor.first_name + mentor.last_name + ".")
    print(Management.fire_mentor(mentor))
    print(mentor.first_name + mentor.last_name + " " + next(story))
    print(next(story))

def main():
    cc_msc = CodecoolClass.create_local()
    mentor = random.choice(cc_msc.mentors)
    mentor_room = Mentor_Room()
    bfa_student = random.choice(cc_msc.students)
    laptop = Laptop()
    pub = Pub("Paprika Pub")
    story_list = read_story_from_file("story.txt")
    story = generate_story_text(story_list)

    play_pub_scene(story, mentor, pub)
    input("Enter to continue. ")
    os.system("clear")
    play_management_scene(story, mentor)
    input("Enter to continue. ")
    os.system("clear")
    play_BFA_scene(story, mentor, mentor_room, bfa_student, laptop)
    input("Enter to continue. ")
    os.system("clear")
    play_ending_scene(story, mentor, mentor_room, bfa_student)

    
    
    

if __name__ == '__main__':
    main()
