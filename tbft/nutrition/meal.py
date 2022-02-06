import uuid

from .food import Food;

class Meal(): 
    def __init__(self, type: str, foods: "list[Food]"):  
        self.uuid = uuid.uuid4()
        self.type = type
        self.foods = foods
        self.cals = self.calculate_cals()

    def calculate_cals(self): 
        cals = 0
        for food in self.foods: 
            cals += food.get_cals()
        return cals

    #getters and setters
    def set_type(self, type): 
        self.type = type

    def get_type(self): 
        return self.type

    def add_food(self, food): 
        self.foods.append(food)
        self.cals = self.calculate_cals()

    def remove_food(self, food): 
        self.foods.remove(food)
        self.cals = self.calculate_cals()

    def get_uuid(self): 
        return self.uuid #no setter, that's definitely not something to modify. 

    def get_cals(self): 
        return self.cals

    def set_cals(self, cals): 
        self.cals = cals

    def get_json(self): 
        {self.uuid: [self.type, self.foods, self.cals]}
