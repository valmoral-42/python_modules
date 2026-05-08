class SecurePlant:
    def __init__(self, name: str):
        self.name = name.capitalize()
        print(f"Plant created: {self.name}")

    def set_height(self, height: int):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        else:
            self.height = height
            print(f"Height updated: {self.height}cm [OK]")

    def set_age(self, age: int):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        else:
            self.age = age
            print(f"Age updated: {self.age} days [OK]")

    def get_info(self):
        print(f"Current plant: {self.name} ({self.height}cm, {self.age} days)")


def ft_garden_security():
    Plant1 = SecurePlant("Rose")

    Plant1.set_height(25)
    Plant1.set_age(30)
    print("")

    Plant1.set_height(-5)
    print("")

    Plant1.get_info()


if __name__ == "__main__":
    print("=== Garden Security System ===")
    ft_garden_security()
