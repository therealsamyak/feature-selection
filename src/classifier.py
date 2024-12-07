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
        self.file_name = file_name
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

        num_columns = len(lines[0].strip().split())
        # Normalize the features in the global_node_map
        self.normalize_features(num_columns)

    def print_global_node_map(self):
        """
        Prints the contents of the global_node_map in a readable format.
        """
        print("Global Node Map:")
        for node_id, node in self.global_node_map.items():
            print(f"ID: {node.id}, Label: {node.label}, Features: {node.features}")

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
            # if nodeID == uniqueID:
            #     continue

            # euclidian distance
            local_dist = sqrt(
                sum(
                    (target - local) ** 2
                    for target, local in zip(
                        target_features, nodeData.features, strict=True
                    )
                )
            )

            if local_dist < global_dist:
                global_dist = local_dist
                closest_node = nodeID

        print("Node", uniqueID, "closest node is Node", closest_node, "with distance", global_dist)
        return self.local_node_map[closest_node].label

    def train(self, uniqueIDArray: List[int], featureSubsetArray: List[int]):
        self.local_node_map = dict()
        self.feature_subset_array = list()

        # account for 0-indexing
        self.feature_subset_array = sorted([x - 1 for x in featureSubsetArray])
        print("Feature Subset:", featureSubsetArray)
        print("Training IDs: ", uniqueIDArray)

        for nodeID in uniqueIDArray:
            nodeData = self.global_node_map[nodeID]

            newNodeData = Item_Node(
                nodeID,
                nodeData.label,
                [nodeData.features[i] for i in self.feature_subset_array],
            )
            self.local_node_map[nodeID] = newNodeData

    def get_number_of_columns(self, number) -> int:
        """
        Determines the number of columns in the dataset by reading the first line.
        """
        with open(self.file_name, "r") as file:  # Use self.file_name
            first_line = file.readline().strip()
            if not first_line:
                raise ValueError("The file is empty or does not contain valid data.")
            return len(first_line.split())

    def get_max_values(self, num_columns: int) -> List[float]:
        """
        Finds the maximum values for each column in the dataset.

        Args:
            num_columns (int): The number of columns in the dataset.

        Returns:
            List[float]: An array where each index contains the maximum value of the corresponding column.
        """
        # Initialize an array with very low values for each column
        max_values = [-float("inf")] * num_columns

        # Open the file and iterate through each line
        with open(self.file_name, "r") as file:
            lines = file.readlines()
            for line in lines:
                values = list(map(float, line.strip().split()))

                # Iterate through each column and update the max value if necessary
                for col in range(num_columns):
                    max_values[col] = max(max_values[col], values[col])

        return max_values

    def get_min_values(self, num_columns: int) -> List[float]:
        """
        Finds the minimum values for each column in the dataset.

        Args:
            num_columns (int): The number of columns in the dataset.

        Returns:
            List[float]: An array where each index contains the minimum value of the corresponding column.
        """

        min_values = [float("inf")] * num_columns

        with open(self.file_name, "r") as file:
            lines = file.readlines()
            for line in lines:
                values = list(map(float, line.strip().split()))

                for col in range(num_columns):
                    min_values[col] = min(min_values[col], values[col])

        return min_values

    def normalize_features(self, num_columns: int):
        """
        Normalizes all columns except the first (class column) and updates the global_node_map.

        Args:
            num_columns (int): The number of columns in the dataset.
        """
        # Get the min and max values for each column
        max_values = self.get_max_values(num_columns)
        min_values = self.get_min_values(num_columns)

        # Iterate through each node in the global_node_map
        for node_id, node in self.global_node_map.items():
            # Normalize each feature except the first column
            normalized_features = [
                (
                    (feature - min_values[i + 1])
                    / (max_values[i + 1] - min_values[i + 1])
                    if max_values[i + 1]
                    != min_values[
                        i + 1
                    ]  # Avoid division by zero omg I hated this shitty error
                    else 0.0
                )  # If all values in the column are the same
                for i, feature in enumerate(node.features)
            ]

            # Update the node with normalized features
            self.global_node_map[node_id] = Item_Node(
                id=node.id, label=node.label, features=normalized_features
            )
