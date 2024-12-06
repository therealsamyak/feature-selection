from math import sqrt


class Classifier:
    def __init__(self, global_node_map):
        self.global_node_map = global_node_map
        self.local_node_map = dict()
        self.feature_subset_array = list()

    def classify(self, uniqueID: int):
        """
        returns Class Label of that ID based on 1-NN
        """

        if not self.local_node_map or not self.feature_subset_array:
            raise ValueError(
                "Model is not trained yet. Please train the model before continuing."
            )

        target_node = self.global_node_map[uniqueID]
        target_features = [target_node.features[i] for i in self.feature_subset_array]

        global_dist = float("inf")
        closest_node = -1

        for nodeID, nodeData in self.local_node_map.items():

            # euclidian distance
            local_dist = sqrt(
                (target - local) ** 2
                for target, local in zip(target_features, nodeData.features)
            )

            if local_dist < global_dist:
                global_dist = local_dist
                closest_node = nodeID

        return self.local_node_map[closest_node].label

    def train(self, uniqueIDArray: list[int], featureSubsetArray: list[int]):
        self.feature_subset_array = sorted(featureSubsetArray)
        pass
