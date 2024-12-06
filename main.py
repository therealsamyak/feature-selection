# import stuff to main as necessary
from feature_search import FeatureDriver
from classifier import Classifier

def main():
    print()
    print("Welcome to Samyak & Ram's Feature Selection Algorithm.")

    total_features = int(input("Please enter total number of features: "))
    if total_features <= 0:
        raise ValueError("The number of features must be a positive integer.")

    print()
    print("Type the number of the algorithm you want to run.")
    print("1. Forward Selection")
    print("2. Backward Elimination")

    choice = int(input("Your choice: "))
    if choice not in (1, 2):
        raise ValueError("Please choose a valid option (1 or 2).")

    test = FeatureDriver(total_features)

    if choice == 1:
        best_node = test.forwards()
        print(
            "\nFinished search!! The best feature subset is",
            best_node.features,
            ", which has an accuracy of",
            best_node.score,
        )
    elif choice == 2:
        best_node = test.backwards()
        print(
            "\nFinished search!! The best feature subset is",
            best_node.features,
            ", which has an accuracy of",
            best_node.score,
        )


if __name__ == "__main__":
    dataset_path = "small-test-dataset.txt"

    # Initialize the classifier with the dataset file
    classifier = Classifier(dataset_path)

    # Example access to a node
    node = classifier.global_node_map[1]
    print(f"Node ID: {node.id}, Label: {node.label}, Features: {node.features}")
