from .validator import *


class Feature_Node:
    def __init__(self, features: list[int], file_name: str, prev=None):
        self.features = sorted(features)  # Automatically sort features
        self.score = Validator(file_name).validate(
            features
        )  # Validate features and compute score
        self.next = []  # Initialize next as an empty list
        self.backward = (
            prev  # Assign the backward link to the provided previous Feature_Node
        )

    def __lt__(self, other):
        if self.score == other.score:
            return len(self.features) > len(other.features)
        return self.score < other.score

    def __gt__(self, other):
        if self.score == other.score:
            return len(self.features) < len(other.features)
        return self.score > other.score

    def __eq__(self, other):
        return self.score == other.score and len(self.features) == len(other.features)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f"Feature_Node(features={self.features}, score={self.score})"
