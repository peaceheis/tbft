class Workout: 
    def __init__(self, cals_burned, muscles_worked: "list[str]"): 
        self.cals_burned = cals_burned
        self.exercises = []
        self.muscles_worked = muscles_worked