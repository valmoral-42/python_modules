import typing
import random


def gen_event(i: int) -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab"
               "move", "climb", "swim", "release"]

    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def data_stream() -> None:
    for i in range(5):
        event = next(gen_event())
        print(f"Event {i}: Player {event[0]} did action {event[1]}")


if __name__ == "__main__":
    "=== Game Data Stream Processor ==="
    data_stream()
