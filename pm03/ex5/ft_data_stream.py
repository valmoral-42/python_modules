from typing import Generator
import random


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab",
               "move", "climb", "swim", "release"]

    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(list_10: list[tuple[str, str]]
                  ) -> Generator[tuple[str, str], None, None]:
    while len(list_10) > 0:
        pos = random.randint(0, len(list_10) - 1)
        yield list_10.pop(pos)


def data_stream() -> None:
    for i in range(1000):
        event = next(gen_event())
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    list_10 = []
    for i in range(10):
        list_10.append(next(gen_event()))
    print(f"Built list of 10 events: {list_10}")

    for event in consume_event(list_10):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {list_10}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    data_stream()
