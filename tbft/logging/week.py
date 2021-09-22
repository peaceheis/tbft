from .day import Day
class Week: 
    def __init__(self): 
        self.days = []
        
    def add_day(self, day): 
        self.days.append(day)

    def get_days(self): 
        return self.days