from classifier import *


class Validator:
    def __init__(self, file_name: str):
        self.classifier: Classifier = Classifier(file_name)
        self.global_map: Dict[int, Item_Node] = self.classifier.global_node_map

    def validate(self, feature_subset_array: List[int]):
        """
        Calculates accuracy of feature_subset using Leave-One-Out validation
        """

        keys = list(self.global_map.keys())
        correctly_classified = 0

        # leave one out validator
        for index, uniqueID in enumerate(keys):
            training_data = keys[:index] + keys[index + 1 :]

            self.classifier.train(training_data, feature_subset_array)

            if self.global_map[uniqueID].label == self.classifier.classify(uniqueID):
                correctly_classified += 1

        return correctly_classified * 1.0 / len(keys)
