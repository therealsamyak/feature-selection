from feature_node import Node


class FeatureDriver:
    def __init__(self, num_features) -> None:
        self.num_features = num_features
        self.global_node = Node([])

    def forwards(self) -> Node:
        self.global_node = Node([])
        prev_node = self.global_node

        while len(prev_node.features) < self.num_features:
            best_node = None

            for index in range(1, self.num_features + 1):
                if index in prev_node.features:
                    continue

                new_features = sorted(prev_node.features + [index])
                curr_node = Node(new_features)

                if best_node is None or curr_node.score > best_node.score:
                    best_node = curr_node

            prev_node = best_node

            if self.global_node.score < best_node.score:
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


test = FeatureDriver(4)
best_node = test.forwards()
print("best subset ", best_node.features, best_node.score)
