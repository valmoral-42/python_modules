class Plant:
        def __init__(self, name: str, height: int, age: int):
            self.name = name.capitalize()
            self.height = height
            self.age = age

        def grow_plant(self, growth: int):
             self.height =+ growth
        
        def age_plant(self, days: int):
             self.age =+ days
        
        def get_info(plant):
             print(f"{plant.name}: {plant.height}cm, {plant.age} days old")

def ft_garden_data():
    Garden = (
         Plant("Rose", 25, 30),
         Plant("Sunflower", 80, 45),
         Plant("Cactus", 15, 120)
    )
    for plant in Garden:
         Plant(plant.get_info())

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    ft_garden_data()
