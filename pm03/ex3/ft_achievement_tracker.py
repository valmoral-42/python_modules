import random


def gen_player_achievements(achievements: list[str]) -> set[str]:
    selection = random.sample(achievements, (random.randint(5, 16)))
    return set(selection)


def achievement_tracker() -> None:
    achievements = ["Crafting Genius", "World Savior", "Master Explorer",
                    "Collector Supreme", "Untouchable", "Boss Slayer",
                    "Strategist", "Speed Runner", "Survivor",
                    "Treasure Hunter", "Unstoppable", "Hidden Path Finder",
                    "First Steps", "Sharp Mind", "This is stopid", "Help"]
    all_achievements = set(achievements)

    alice = gen_player_achievements(achievements)
    bob = gen_player_achievements(achievements)
    charlie = gen_player_achievements(achievements)
    dylan = gen_player_achievements(achievements)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print("")

    distinct_achievements = alice | bob | charlie | dylan
    common_achievements = alice & bob & charlie & dylan

    print(f"All distinct achievements: {distinct_achievements}")
    print("")
    print(f"Common achievements: {common_achievements}")
    print("")

    print(f"Only Alice has: {alice - bob - charlie - dylan}")
    print(f"Only Bob has: {bob - alice - charlie - dylan}")
    print(f"Only Charlie has: {charlie - bob - alice - dylan}")
    print(f"Only Dylan has: {dylan - bob - charlie - alice}")
    print("")

    print(f"Alice is missing: {all_achievements - alice}")
    print(f"Bob is missing: {all_achievements - bob}")
    print(f"Charlie is missing: {all_achievements - charlie}")
    print(f"Dylan is missing: {all_achievements - dylan}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print("")
    achievement_tracker()
