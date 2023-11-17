class Time:
    def __init__(self, time):
        self.sec = time

    def seconds_to_minutes(self):
        min = self.sec // 60
        s = self.sec % 60
        return (str(min) + " min " + str(s) + " sec")

    def seconds_to_hours(self):
        hour = self.sec // (60 * 60)
        min = (self.sec - (hour * 3600)) // 60
        s = self.sec - (hour * 3600) - (min * 60)
        return (str(hour) + " hrs " + str(min) + " min " + str(s) + " sec")

    def seconds_to_days(self):
        day = self.sec // (60 * 60 * 24)
        hour = (self.sec - (day * 3600 * 24)) // (60 * 60)
        min = (self.sec - (day * 3600 * 24) - (hour * 3600)) // 60
        s = self.sec - (day * 3600 * 24) - (hour * 3600) - (min * 60)
        return (str(day) + " days " + str(hour) + " hrs " + str(min) + " min " + str(s) + " sec")
