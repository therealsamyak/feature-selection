import time

from .classifier import *


class Validator:
    def __init__(self, file_name: str):
        self.classifier: Classifier = Classifier(file_name)
        self.global_map: Dict[int, Item_Node] = self.classifier.global_node_map

    def validate(self, feature_subset_array: List[int]) -> int:
        """
        Calculates accuracy of feature_subset using Leave-One-Out validation
        """
        accuracy = 0

        if (len(feature_subset_array)) > 0:
            keys = list(self.global_map.keys())
            correctly_classified = 0

            # leave one out validator
            for index, uniqueID in enumerate(keys):

                # train classifier
                training_data = keys[:index] + keys[index + 1 :]
                self.classifier.train(training_data, feature_subset_array)

                # check accuracy
                if (
                    abs(
                        self.global_map[uniqueID].label
                        - self.classifier.classify(uniqueID)
                    )
                    < 0.1
                ):
                    correctly_classified += 1

            accuracy = correctly_classified * 1.0 / len(keys)

        else:
            accuracy = 0
            return accuracy

        return accuracy
