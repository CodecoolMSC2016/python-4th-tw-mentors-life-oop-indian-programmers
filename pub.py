import random


class Pub():

    def __init__(self, name):
        self.name = name
        self.mood_level = random.randint(0, 100)
        self.number_of_people = random.randint(1, 30)
        self.music_playing = False
        self.free_tables = bool(random.randint(0, 2))
        self.chance_for_pub_fight = round((self.mood_level / 30) * (self.number_of_people / 5))

    def calc_chance_for_fight(self):
        self.chance_for_pub_fight = round(((self.mood_level*10) / 30) * (self.number_of_people / 5))
        return "Chance for a fight is " + str(self.chance_for_pub_fight) + "%!"

    def handle_pub_fight(self):
        self.number_of_people = 0
        return "There are no more people left in the pub."

    def change_music(self):
        self.music_playing = True
        music_list = []
        with open("music_list.txt") as f:
            for line in f:
                music_list.append(line)
        return random.choice(music_list).strip() + " is playing in the pub now."

    def serve_alcohol(self):
        self.mood_level += 5
        return "The overall mood increased to " + str(self.mood_level)
