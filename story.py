from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from laptop import Laptop
from pub import Pub
from management import Management
from mentor_room import Mentor_Room
import os


codecool_bp = CodecoolClass.create_local()

input("Turn on laptop? ")
laptop = Laptop()
for msg in laptop.turn_on():
    os.system("clear")
    print(msg)
