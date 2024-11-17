from feature_node import Node


class FeatureDriver:
    def __init__(self, num_features) -> None:
        self.num_features = num_features
        self.global_node = Node([])

    def forwards(self) -> Node:
        self.global_node = Node([])

        while len(self.global_node.features) < self.num_features:
            best_node = None

            for index in range(1, self.num_features + 1):
                if index in self.global_node.features:
                    continue

                new_features = self.global_node.features + [index]
                curr_node = Node(new_features)

                if best_node is None or curr_node.score > best_node.score:
                    best_node = curr_node

            if self.global_node.score < best_node.score:
                self.global_node = best_node

        return self.global_node


test = FeatureDriver(4)
best_node = test.forwards()
print("best subset ", best_node.features, best_node.score)
