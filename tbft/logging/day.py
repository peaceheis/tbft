from datetime import date

from tbft.serialization.serializable import Serializable
from tbft.nutrition.meal import Meal
from tbft.activity.activity import Activity

class Day(Serializable): 
    def __init__(self, date: date): 
        self.date = date
        self.meals: "list[Meal]" = []
        self.activities: "list[Activity]" = []
        self.hours_sleep = 0

    def add_meal(self, meal): 
        self.meals.append(meal)

    def remove_meal(self, meal): 
        self.meals.remove(meal)

    def get_meals(self): 
        return self.meals
        
    def add_activity(self, activity): 
        self.activities.append(activity)

    def remove_activity(self, activity): 
        self.activities.remove(activity)
        
    def get_activities(self): 
        return self.activities

    def set_sleep(self, hours: float): 
        self.sleep = hours

    def get_json(self): 
        return {self.date.strftime("%Y %m %d"): []}


