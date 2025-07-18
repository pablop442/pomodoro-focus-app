
class PomodoroTimer:
    def __init__(self, work=25, break_time=5):
        self.work_minutes = work
        self.break_minutes = break_time
        self.is_running = False
        self.is_break = False
        self.remaining_seconds = work * 60

    def start(self):
        self.is_running = True
        self.is_break = False
        self.remaining_seconds = self.work_minutes * 60

    def start_break(self):
        self.is_running = True
        self.is_break = True
        self.remaining_seconds = self.break_minutes * 60

    def stop(self):
        self.is_running = False
        self.remaining_seconds = self.work_minutes * 60

    def tick(self):
        if self.is_running and self.remaining_seconds > 0:
            self.remaining_seconds -= 1

    def get_time(self):
        minutes = self.remaining_seconds // 60
        seconds = self.remaining_seconds % 60
        return f"{minutes:02d}:{seconds:02d}"