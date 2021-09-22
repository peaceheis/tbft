class Muscle_Exercise_Group: 
    def __init__(self, muscle): 
        self.muscle = muscle
        self.exercises = []

    def add_exercise(self, exercise): 
        self.exercises.append(exercise)
    
    def remove_exercise(self, exercise): 
        self.exercise.remove(exercise)

    