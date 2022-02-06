from dataclasses import dataclass

from tbft.serialization.serializable import Serializable
from tbft.activity.exercise_variation import Exercise_Variation

@dataclass
class Exercise(Serializable): 
    __slots__ = ["name", "variations", "notes"]
    name: str
    variations: "list[Exercise_Variation]"
    notes: str

    def as_json_ready(self):
        return [self.name, self.variations, self.notes]

    @classmethod
    def from_json(cls, json):
        cls.__init__(json[0], 
                    [Exercise_Variation.from_json(var) for var in json[1]], 
                    json[2])