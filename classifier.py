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
        """
        Reads the content from file and populates the global_node_map.
        Each line in the file corresponds to an Item_Node.
        """
        with open(file_name, "r") as file:
            lines = file.readlines()
            for idx, line in enumerate(lines, start=1):
                values = line.strip().split()
                label = int(float(values[0]))  # First column is the class label
                features = list(
                    map(float, values[1:])
                )  # Remaining columns are features

                # Create an Item_Node and add it to the global_node_map
                self.global_node_map[idx] = Item_Node(
                    id=idx, label=label, features=features
                )

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
                sum(
                    (target - local) ** 2
                    for target, local in zip(target_features, nodeData.features)
                )
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
