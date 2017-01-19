from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from laptop import Laptop
from pub import Pub
from management import Management
from mentor_room import Mentor_Room
import os


codecool_bp = CodecoolClass.create_local()
# for student in codecool_bp.students:
#   print(student.first_name + student.last_name)
zita = codecool_bp.find_student_by_full_name("Zita Para")

print(zita.gender)
paprika = Pub()
mentor_room = Mentor_Room()

input("Turn on laptop? ")
laptop = Laptop()
for msg in laptop.turn_on():
    os.system("clear")
    print(msg)
