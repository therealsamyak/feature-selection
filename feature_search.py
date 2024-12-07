from feature_node import *


class FeatureDriver:
    def __init__(self, num_features) -> None:
        self.num_features = num_features
        self.global_node = Feature_Node([], None)

    def forwards(self) -> Feature_Node:
        self.global_node = Feature_Node([], None)
        print()
        print(
            f"Feature set {self.global_node.features} is initially the best, accuracy is {self.global_node.score}"
        )
        print()

        prev_node = self.global_node

        while len(prev_node.features) < self.num_features:
            best_node = None

            for index in range(1, self.num_features + 1):
                if index in prev_node.features:
                    continue

                new_features = sorted(prev_node.features + [index])
                curr_node = Feature_Node(new_features, prev_node)
                print(
                    f"Using feature(s) {curr_node.features}, the accuracy is {curr_node.score}"
                )

                if not best_node or curr_node > best_node:
                    best_node = curr_node

            prev_node = best_node

            if self.global_node < best_node:
                self.global_node = best_node
                print()
                print(
                    f"Feature set {self.global_node.features} is a NEW best, accuracy is {self.global_node.score}"
                )
                print()
            else:
                print()
                print(
                    f"Feature set {best_node.features} was best at this level, accuracy is {best_node.score}"
                )
                print(
                    f"Feature set {self.global_node.features} is still the overall best, accuracy is {self.global_node.score}"
                )
                print()

        return self.global_node

    def backwards(self) -> Feature_Node:
        self.global_node = Feature_Node(list(range(1, self.num_features + 1)), None)
        print()
        print(
            f"Feature set {self.global_node.features} is initially the best, accuracy is {self.global_node.score}"
        )
        print()

        prev_node = self.global_node

        while len(prev_node.features) > 0:
            best_node = None

            for index in prev_node.features:
                new_features = [f for f in prev_node.features if f != index]

                curr_node = Feature_Node(sorted(new_features), prev_node)

                print(
                    f"Using feature(s) {curr_node.features}, the accuracy is {curr_node.score}"
                )

                if best_node is None or curr_node > best_node:
                    best_node = curr_node

            prev_node = best_node

            if self.global_node < best_node:
                self.global_node = best_node
                print()
                print(
                    f"Feature set {self.global_node.features} is a NEW best, accuracy is {self.global_node.score}"
                )
                print()
            else:
                print()
                print(
                    f"Feature set {best_node.features} was best at this level, accuracy is {best_node.score}"
                )
                print(
                    f"Feature set {self.global_node.features} is still the overall best, accuracy is {self.global_node.score}"
                )
                print()

        return self.global_node

    def userInputDriver(self):
        print()
        print("Welcome to Samyak & Ram's Feature Selection Algorithm.")

        total_features = int(input("Please enter total number of features: "))
        if total_features <= 0:
            raise ValueError("The number of features must be a positive integer.")

        print()
        print("Type the number of the algorithm you want to run.")
        print("1. Forward Selection")
        print("2. Backward Elimination")

        choice = int(input("Your choice: "))
        if choice not in (1, 2):
            raise ValueError("Please choose a valid option (1 or 2).")

        test = FeatureDriver(total_features)

        if choice == 1:
            best_node = test.forwards()
            print(
                "\nFinished search!! The best feature subset is",
                best_node.features,
                ", which has an accuracy of",
                best_node.score,
            )
        elif choice == 2:
            best_node = test.backwards()
            print(
                "\nFinished search!! The best feature subset is",
                best_node.features,
                ", which has an accuracy of",
                best_node.score,
            )
