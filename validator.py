import random


def feature_validator(features: list[int]) -> int:
    accuracy = random.randint(0, 100)
    print(f"Using feature(s) {features}, the accuracy is {accuracy}")
    return accuracy
