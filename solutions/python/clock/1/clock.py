class Clock:
    def __init__(self, hour, minute):
        self.minutes: int = (60 * hour + minute) % (60*24)

    def __repr__(self):
        return f'Clock({(self.minutes // 60) % 24}, {self.minutes % 60})'

    def __str__(self):
        return f'{(self.minutes // 60) % 24:02d}:{self.minutes % 60:02d}'

    def __eq__(self, other):
        return self.minutes == other.minutes

    def __add__(self, minutes):
        return Clock(0, self.minutes + minutes)

    def __sub__(self, minutes):
        return Clock(0, self.minutes - minutes)
