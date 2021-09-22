import uuid

from .activity import Activity 

class Workout(Activity): 
    def __init__(self, name="Workout", cals_burned=0, muscles_worked: "list[str]"=[""]): 
        self.uuid = uuid.uuid4()
        self.name = name
        self.cals = cals_burned
        self.exercises = [""]
        self.muscles_worked = muscles_worked

    def get_uuid(self): 
        return self.uuid

    def get_json(self):
        return super().get_json()[self.uuid]#.append(self.exercises).append(self.muscles_worked)

t = Workout(100, ["Back", "Biceps"])
print(t.get_json())