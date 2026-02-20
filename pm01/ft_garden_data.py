class Plant:
        def __init__(self, name: str, height: int, age: int):
            self.name = name.capitalize()
            self.height = height
            self.age = age

def ft_garden_data():
    Garden = (
         Plant("Rose", 25, 30),
         Plant("Sunflower", 80, 45),
         Plant("Cactus", 15, 120)
    )
    for plant in Garden:
         print(f"{plant.name}: {plant.height}cm, {plant.age} days old")

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    ft_garden_data()
