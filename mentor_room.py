import random


class Mentor_Room():

    def __init__(self):
        self.bfa_running = False
        self.is_clean = True
        self.mood_level = random.randint(0, 100)
        self.window_open = False

    def gets_dirty(self):
        self.is_clean = False
        return "The room is covered in dirt now."

    def open_window(self):
        if self.is_clean == False:
            self.window_open = True
            self.clean = True
            return "The window is now open, and the room smells cleaner."

    def start_bfa(self):
        self.bfa_running = True
        return "BFA has started"

    def stop_bfa(self):
        self.bfa_running = False
        return "BFA has stopped"
