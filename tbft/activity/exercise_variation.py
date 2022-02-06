from dataclasses import dataclass

from tbft.serialization.serializable import Serializable

@dataclass
class Exercise_Variation(Serializable): 
    __slots__ = ["name", "muscles_targeted", "performance", "notes"]
    name: str
    muscles_targeted: "list[list[str]]"
    performance: "list[str]" # setXrepsX[weight]
    notes: str

    def as_json_ready(self): 
        return {self.name, self.muscles_targeted, self.performance, self.notes}
    
    @classmethod
    def from_json(cls, json: list): 
        cls.__init__(json[0], json[1], json[3])