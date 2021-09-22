class Exercise: 
    def __init__(self, target_muscles, reps, weight=0): 
        self.reps = reps
        self.target_muscles = target_muscles
        self.weight = weight

    def get_reps(self): 
        return self.reps

    def set_reps(self, reps): 
        self.reps = reps

    def get_target_muscles(self): 
        return self.target_muscles

    def set_target_muscles(self, target_muscles): 
        self.target_muscles = target_muscles

    def get_weight(self): 
        return self.weight

    def set_weight(self, weight): 
        self.weight = weight