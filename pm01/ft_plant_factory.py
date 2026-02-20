class Plant:
    i = 0

    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age
        Plant.i += 1
        print(f"Created: {self.name} ({self.height}cm, {self.age} days old)")


def ft_plant_factory():
    Plant("rose", 25, 30)
    Plant("Sunflower", 80, 45)
    Plant("Cactus", 15, 120)
    Plant("tulip", 45, 60)
    Plant("Daisy", 50, 50)

    print(f"\nTotal plants created: {Plant.i}")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    ft_plant_factory()
