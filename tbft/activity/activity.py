import uuid

class Activity: 
    def __init__(self, name, cals=0): 
        self.uuid = uuid.uuid4()
        self.name = name
        self.cals = cals

    def set_name(self, name): 
        self.name = name

    def get_name(self): 
        return self.name

    def set_cals(self, cals): 
        self.cals = cals

    def get_cals(self): 
        return self.cals

    def get_json(self): 
        return {self.uuid: [self.name, self.cals]}