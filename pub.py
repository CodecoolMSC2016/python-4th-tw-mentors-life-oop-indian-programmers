class Pub():
    def __init__(self, mood_level, number_of_people, music_playing, free_tables, chance_for_pub_fight):
        self.mood_level = mood_level
        self.number_of_people = number_of_people
        self.music_playing = music_playing
        self.free_tables = free_tables
        self.chance_for_pub_fight = chance_for_pub_fight

    def handle_pub_fight(self):
        self.number_of_people = 0
        return "There are no more people left in the pub."

    def change_music(self):
        self.music_playing = True
