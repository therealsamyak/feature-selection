# import stuff to main as necessary
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
    test = FeatureDriver("datasets/small-test-dataset.txt")
    test.userInputDriver()

    return


if __name__ == "__main__":
    main()
