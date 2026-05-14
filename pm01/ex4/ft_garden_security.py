class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age
        print(f"Plant created: {self.name}: {self.height:.1f}cm, "
              f"{self.age} days old")

    def set_height(self, height: float):
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        else:
            self.height = height
            print(f"Height updated: {self.height}cm")

    def set_age(self, age: int):
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        else:
            self.age = age
            print(f"Age updated: {self.age} days")

    def show(self):
        print(f"Current state: {self.name}: {self.height:.1f}cm, "
              f"{self.age} days")


def ft_garden_security():
    p1 = Plant("Rose", 15, 10)
    print("")
    p1.set_height(25)
    p1.set_age(30)
    print("")
    p1.set_height(-25)
    p1.set_age(-30)
    print("")
    p1.show()


if __name__ == "__main__":
    print("=== Garden Security System ===")
    ft_garden_security()
