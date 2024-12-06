from math import sqrt


class Classifier:
    def __init__(self, global_node_map):
        self.global_node_map = global_node_map
        self.local_node_map = None
        self.feature_subset_array = None

    def classify(self, uniqueID):

        if not self.local_node_map or not self.feature_subset_array:
            raise ValueError(
                "Model is not trained yet. Please train the model before continuing."
            )

        target_node = self.global_node_map[uniqueID]
        target_features = [target_node.features[i] for i in self.feature_subset_array]

        global_dist = float("inf")
        closest_node = None

        for nodeID, nodeData in self.local_node_map.items():
            local_dist = sqrt(
                (target - local) ** 2
                for target, local in zip(target_features, nodeData.features)
            )

            if local_dist < global_dist:
                global_dist = local_dist
                closest_node = nodeID

        return self.local_node_map[closest_node].label

    def train(self, uniqueIDArray, featureSubsetArray):
        self.feature_subset_array = sorted(featureSubsetArray)
        pass
