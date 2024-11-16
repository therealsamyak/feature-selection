import Node from feature_node

class FeatureDriver:
    def __init__(self, num_features):
        self.num_features = num_features
        self.global_high = 0
        self.global_features = []
    
    def forwards(self, num_features):
        self.global_high = 0
        self.global_features = []

        start = Node
        for feature in range(len(num_features)):



