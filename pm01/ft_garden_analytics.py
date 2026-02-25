class Plant:
    def __init__(self, name: str):
        self.name = name.title()
        print(f"Added {self.name} to Alice's Garden")

    def set_height(self, height: int):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            return
        else:
            self.height = height

    def grow_plant(self, growth: int):
        self.height += growth
        print(f"{self.name} grew {growth}cm")


class Tree(Plant):
    def __init__(self, name: str, height: int):
        super().__init__(name)
        self.set_height(height)

    def get_info(self):
        print(f"- {self.name}: {self.height}cm")


class Flower(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name)
        self.set_height(height)
        self.color = color

    def get_info(self):
        print(f"- {self.name}: {self.height}cm, {self.color} "
              "flowers (blooming)")


def ft_garden_analytics():
    Tree1 = Tree("oak tree", 99)
    Flower1 = Flower("rose", 25, "red")
    Flower2 = Flower("sunflower", 48, "yellow")
    print("")

    print("Alice is helping all plants grow...")
    Tree1.grow_plant(2)
    Flower1.grow_plant(1)
    Flower2.grow_plant(3)
    print("")

    print("=== Alice's Garden Report ===")
    print("Plants in garden:")
    Tree1.get_info()
    Flower1.get_info()
    Flower2.get_info()


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print("")
    ft_garden_analytics()
