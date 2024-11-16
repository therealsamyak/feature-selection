from validator import feature_validator  

class Node:
    def __init__(self, features: list[int]):
        self.features = features  
        self.score = feature_validator(features) 
        self.forward = None 
        self.backward = None 