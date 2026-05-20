import math


def get_player_pos() -> None:
    while True:
        coordinates = input("Enter new coordinates as floats "
                            "in format 'x,y,z': ")
        user_coordinates = coordinates.split(",")
        if len(user_coordinates) == 3:
            try:
                valid_coordinates = []
                for coordinate in user_coordinates:
                    valid_coordinates.append(float(coordinate))
            except ValueError:
                print(f"Error on parameter '{coordinate}': could not "
                      f"convert string to float: '{coordinate}'")
                continue
            coordinates = tuple(valid_coordinates)
            return coordinates
        else:
            print("Invalid syntax")


def coordinate_system() -> None:
    print("Get a first set of coordinates")
    coordinates = get_player_pos()
    x1, y1, z1 = coordinates
    print(f"Got a first tuple: {coordinates}")
    print(f"it includes: X={x1}, Y={y1}, Z={z1}")
    distance = round((math.sqrt(x1**2 + y1**2 + z1**2)), 4)
    print(f"Distance to center: {distance}")
    print("")

    print("Get a second set of coordinates")
    coordinates = get_player_pos()
    x2, y2, z2 = coordinates
    distance = round((math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)), 4)
    print(f"Distance between the 2 sets of coordinates: {distance}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("")
    coordinate_system()
