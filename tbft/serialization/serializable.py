import json

class Serializable: 
    def __init__(self): 
        self.as_dict = {}

    def as_json_ready(self): 
        pass

    @classmethod
    def from_json(cls, json): 
        pass