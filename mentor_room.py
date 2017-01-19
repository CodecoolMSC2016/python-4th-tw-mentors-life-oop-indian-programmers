class Mentor_Room():
    def __init__(self, bfa_running, is_clean=True, mood_level, window_open):
        self.bfa_running = bfa_running
        self.is_clean = is_clean
        self.mood_level = mood_level
        self.window_open = window_open
        
    def open_window(self):
        if self.is_clean == False:
            self.window_open = True
            self.clean = True
