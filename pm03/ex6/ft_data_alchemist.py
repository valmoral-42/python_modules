import random


def data_alchemist() -> None:
    names = ["Alice", "bob", "Charlie", "dylan", "Emma",
             "Gregory", "john", "kevin", "Liam"]
    all_cap = [name.capitalize() for name in names]
    only_cap = [name for name in names if name == name.capitalize()]

    print(f"Initial list of players: {names}")
    print(f"New list with all names capitalized: {all_cap}")
    print(f"New list of capitalized names only: {only_cap}")
    print("")

    scores = {name: random.randint(0, 1000) for name in all_cap}
    print(f"Score dict: {scores}")
    avg = round(sum(scores.values())/len(names), 2)
    print(f"Score average is {avg}")
    high = {name: score for name, score in scores.items() if score > avg}
    print(f"High scores: {high}")


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print("")
    data_alchemist()
