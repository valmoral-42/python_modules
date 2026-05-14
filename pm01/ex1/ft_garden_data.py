class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data():
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)
    garden = [p1, p2, p3]

    for plant in garden:
        plant.show()


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    ft_garden_data()
