import sys


def inventory_system() -> None:
    inventory = {}

    for i in range(1, len(sys.argv)):
        args = sys.argv[i]
        inv_split = args.split(":")
        if len(inv_split) == 2:
            item = inv_split[0]
            value = inv_split[1]
            if item in inventory:
                print(f"Redundant item '{item}' - discarting")
            else:
                try:
                    inventory[item] = int(value)
                except ValueError as e:
                    print(f"Quantity error for '{item}': {e}")
        else:
            print(f"Error - invalid parameter '{args}'")

    if not inventory:
        print("Inventory is empty. Add something!")
        return

    sum_all = sum(inventory.values())

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)}"
          f" items: {sum_all}")

    most = list(inventory.keys())[0]
    least = list(inventory.keys())[0]

    for item in inventory:
        percentage = (inventory[item]/sum_all)*100
        print(f"Item {item} represents "
              f"{round(percentage, 1)}%")
        if inventory[item] > inventory[most]:
            most = item
        if inventory[item] < inventory[least]:
            least = item

    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory {inventory}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory_system()
