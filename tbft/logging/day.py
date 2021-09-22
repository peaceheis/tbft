from datetime import date
from tbft.nutrition.meal import Meal

class Day: 
    def __init__(self, date: date): 
        self.date = date
        self.meals: "list[Meal]" = []
        self.sleep = 0

    def add_meal(self, meal): 
        self.meals.append(meal)

    def remove_meal(self, meal): 
        self.meals.remove(meal)

    def get_meals(self): 
        return self.meals

    def set_sleep(self, hours: float): 
        self.sleep = hours

    def get_json(self): 
        return {self.date.strftime("%Y%m%d"): []}

