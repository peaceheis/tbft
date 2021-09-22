from .week import Week 
class Month: 
    def __init__(self): 
        self.weeks = []

    def add_week(self, week): 
        self.weeks.append(week)

    def get_weeks(self): 
        return self.weeks