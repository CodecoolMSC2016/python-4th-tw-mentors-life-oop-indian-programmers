import random
class Mentor_Room():
    def __init__(self):
        self.bfa_running = False
        self.is_clean = True
        self.mood_level = random.randint(0,100)
        self.window_open = False

    def open_window(self):
        if self.is_clean == False:
            self.window_open = True
            self.clean = True
            
    def start_bfa(self):
        self.bfa_running= True
