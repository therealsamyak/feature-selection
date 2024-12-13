# Group: Samyak Kakatur - skaka008 - Session 1, Ram Rao - rrao011 - Session 1
#
# Small Dataset Results:
# - Forward: {3, 5}, Acc: 0.92
# - Backward: {3, 5}, Acc: 0.92
#
# Large Dataset Results:
# - Forward: {1, 27}, Acc: 0.955
# - Backward: {1, 27}, Acc: 0.955
#
# Titanic
# - Forward: {2}, Acc: 0.78
# - Backward: {2}, Acc: 0.78

from src import *


def main():
    # Part 2

    # small data set
    # dataset_path = "datasets/small-test-dataset.txt"
    # test_validator = Validator(dataset_path)
    # print(test_validator.validate([3, 5, 7]))

    # large data set
    # dataset_path = "datasets/large-test-dataset.txt"
    # test_validator = Validator(dataset_path)
    # test_validator.validate([1, 3, 5])

    # Final Part
    test = FeatureDriver("datasets/titanic.txt")
    test.userInputDriver()

    return


if __name__ == "__main__":
    main()
