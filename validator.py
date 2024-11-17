import random

random.seed(10)

def feature_validator(features: list[int]) -> int:
    if (len(features) <= 0):
        return 0
    accuracy = random.randint(0, 100)
    print(f"Using feature(s) {features}, the accuracy is {accuracy}")
    return accuracy
