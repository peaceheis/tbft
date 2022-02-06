from datetime import date

from tbft.activity.workout import Workout
from tbft.serialization.serializable import Serializable

class TBFTInstance(Serializable): 
    def __init__(self, version: str = date.today.isoformat()): 
        self.version = version
        self.workouts: "list[Workout]" = []

    def start_gui(self): 
        pass

    def as_json_ready(self):
        return [
            self.version, 
            []
        ]

    @classmethod
    def from_json(cls, json):
        return super().from_json(json)