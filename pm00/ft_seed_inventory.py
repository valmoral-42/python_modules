def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (unit == "packets"):
        print(str.capitalize(seed_type), "seeds:", quantity, unit, "available")
    elif (unit == "grams"):
        print(str.capitalize(seed_type), "seeds:", quantity, unit, "total")
    elif (unit == "area"):
        print(str.capitalize(seed_type),
              "seeds: covers", quantity, "square meters")
    else:
        print("Unknown unit type")
