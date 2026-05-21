import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab",
               "move", "climb", "swim", "release"]

    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(prev_list: list[tuple[str, str]]) -> None:
    new_list = prev_list.copy()
    random.shuffle(prev_list)
    for event in prev_list:
        print(f"Got event from list: {event}")
        new_list.remove(event)
        print(f"Remains in list: {new_list}")


def data_stream() -> None:
    for i in range(1000):
        event = next(gen_event())
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    list_10 = []
    for i in range(5):
        list_10.append(next(gen_event()))
    print(f"Built list of 10 events: {list_10}")

    consume_event(list_10)


if __name__ == "__main__":
    "=== Game Data Stream Processor ==="
    data_stream()
