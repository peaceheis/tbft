from dataclasses import dataclass

from tbft.serialization.serializable import Serializable

@dataclass
class Workout(Serializable): 
    name: str
    date: str
    __slots__ = ["name", "date"]
    def as_json_ready(self):
        return super().as_json_ready()

    @classmethod
    def from_json(cls, json):
        return super().from_json(json)