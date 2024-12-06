from math import sqrt
from typing import Dict, List


class Item_Node:
    def __init__(self, id: int, label: int, features: List[float]):
        self.id = id
        self.label = label
        self.features = features


class Classifier:
    def __init__(self, file_name):
        self.global_node_map: Dict[int, Item_Node] = {}
        self.local_node_map: Dict[int, Item_Node] = {}
        self.feature_subset_array: List[int] = []
        self.createItemNodeMap(file_name)

    def createItemNodeMap(self, file_name: str):
        pass

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

    def train(self, uniqueIDArray: List[int], featureSubsetArray: List[int]):
        self.feature_subset_array = sorted(featureSubsetArray)

        for nodeID in uniqueIDArray:
            nodeData = self.global_node_map[nodeID]

            newNodeData = Item_Node(
                nodeID,
                nodeData.label,
                [nodeData.features[i - 1] for i in self.feature_subset_array],
            )

            self.local_node_map[nodeID] = newNodeData
