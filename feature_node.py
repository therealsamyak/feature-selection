from validator import feature_validator


class Node:
    def __init__(self, features: list[int], prev=None):
        self.features = sorted(features)  # Automatically sort features
        self.score = feature_validator(self.features)  # Validate features and compute score
        self.next = []  # Initialize next as an empty list
        self.backward = prev  # Assign the backward link to the provided previous Node

    @classmethod
    def from_existing(cls, features: list[int], prev: 'Node'):
        return cls(features, prev)

    def __lt__(self, other):
        return self.score < other.score

    def __le__(self, other):
        return self.score <= other.score

    def __gt__(self, other):
        return self.score > other.score

    def __ge__(self, other):
        return self.score >= other.score

    def __eq__(self, other):
        return self.score == other.score

    def __ne__(self, other):
        return self.score != other.score

    def __repr__(self):
        return f"Node(features={self.features}, score={self.score})"
