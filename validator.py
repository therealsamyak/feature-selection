import random

random.seed(10)


def feature_validator(features: list[int]) -> int:
    if len(features) <= 0:
        return 0
    accuracy = random.randint(1, 100)
    print(f"Using feature(s) {features}, the accuracy is {accuracy}")
    return accuracy


# use this if always want increasing score

# glob_score = 1
# def feature_validator(features: list[int]) -> int:
#     global glob_score
#     if len(features) <= 0:
#         return 0
#     accuracy = glob_score
#     glob_score += 1
#     print(f"Using feature(s) {features}, the accuracy is {accuracy}")
#     return accuracy
