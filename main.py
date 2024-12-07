# import stuff to main as necessary
from src import *

def main():
    # Part 1
    # FeatureDriver.userInputDriver()

    # Part 2
    dataset_path = "datasets/small-test-dataset.txt"
    test_validator = Validator(dataset_path)
    print(test_validator.validate([3, 5, 7]))

    return


if __name__ == "__main__":
    main()
