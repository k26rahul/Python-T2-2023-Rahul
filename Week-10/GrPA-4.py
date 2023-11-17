class Time:
    def __init__(self, time):
        self.time = time

    def seconds_to_minutes(self):
        seconds = self.time % 60
        minutes = self.time // 60
        return f'{minutes} min {seconds} sec'

    def seconds_to_hours(self):
        hours = self.time // 3600
        seconds = (self.time - hours * 3600) % 60
        minutes = (self.time - hours * 3600) // 60
        return f'{hours} hrs {minutes} min {seconds} sec'

    def seconds_to_days(self):
        days = self.time // 86400
        hours = (self.time - days * 86400) // 3600
        seconds = (self.time - days * 86400 - hours * 3600) % 60
        minutes = (self.time - days * 86400 - hours * 3600) // 60
        return f'{days} days {hours} hrs {minutes} min {seconds} sec'
