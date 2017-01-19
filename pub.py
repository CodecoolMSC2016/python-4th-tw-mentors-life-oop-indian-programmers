import random


class Pub():

    def __init__(self):
        self.mood_level = random.randint(0, 100)
        self.number_of_people = random.randint(1, 30)
        self.music_playing = True
        self.free_tables = bool(random.randint(0, 2))
        self.chance_for_pub_fight = (self.mood_level / 30) * (self.number_of_people / 5)

    def handle_pub_fight(self):
        self.number_of_people = 0
        return "There are no more people left in the pub."

    def change_music(self):
        self.music_playing = True
