# import stuff to main as necessary
from src import *


def main():
    # Part 1
    # FeatureDriver.userInputDriver()

    # Part 2

    # small data set
    # dataset_path = "datasets/small-test-dataset.txt"
    # test_validator = Validator(dataset_path)
    # print(test_validator.validate([3, 5, 7]))

    # large data set
    dataset_path = "datasets/small-test-dataset.txt"
    test_validator = Validator(dataset_path)
    test_validator.validate([1, 15, 27])

    return


if __name__ == "__main__":
    main()
