import uuid

class Food:
    def __init__(self, name, cals, carb=0, protein=0, fat=0): 
        self.uuid = uuid.uuid4()
        self.name: str = name
        self.cals = cals
        self.carb = 0
        self.protein = 0
        self.fat = 0

    def get_json(self): 
        return {self.uuid: [self.name, self.cals, self.carb, self.protein, self.fat]}

    #getters and setters

    def get_cals(self): 
        return self.cals

    def set_cals(self, cals): 
        self.cals = cals

    def get_carb(self): 
        return self.carb

    def set_carb(self, carb): 
        self.carb = carb

    def get_protein(self): 
        return self.protein

    def set_protein(self, protein): 
        self.protein = protein

    def get_fat(self): 
        return self.fat

    def set_fat(self, fat): 
        self.fat = fat









