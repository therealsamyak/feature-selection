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

        start_time = time.time_ns()

        keys = list(self.global_map.keys())
        correctly_classified = 0

        # leave one out validator
        for index, uniqueID in enumerate(keys):
            iteration_start_time = time.time_ns()

            # train classifier
            training_data = keys[:index] + keys[index + 1 :]
            self.classifier.train(training_data, feature_subset_array)

            # check accuracy
            if (
                abs(
                    self.global_map[uniqueID].label - self.classifier.classify(uniqueID)
                )
                < 0.1
            ):
                iteration_end_time = time.time_ns()
                print(
                    "Correctly Classified in "
                    + str(iteration_end_time - iteration_start_time)
                    + " nanoseconds!\n"
                )
                correctly_classified += 1
            else:
                iteration_end_time = time.time_ns()
                print(
                    "Incorrectly Classified in "
                    + str(iteration_end_time - iteration_start_time)
                    + " nanoseconds.\n"
                )

        end_time = time.time_ns()
        accuracy = correctly_classified * 1.0 / len(keys)
        print("Overall accuracy is", accuracy)
        print("Finished validation in", end_time - start_time, "nanoseconds")
        return accuracy
