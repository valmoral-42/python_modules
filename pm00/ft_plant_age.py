def ft_plant_age():
    days = int(input("Enter plant age in days: "))
    if days <= 60:
        print("Plant needs more time to grow.")
    if days > 60:
        print("Plant is ready to harvest!")
