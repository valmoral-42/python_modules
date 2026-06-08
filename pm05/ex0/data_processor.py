from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self):
        super().__init__()
        self._storage = []
        self._current_rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, Any]:
        if not self._storage:
            return (0, "")

        output_data = self._storage.pop(0)
        self._current_rank += 1

        return (self._current_rank, output_data)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(
                isinstance(item, (int, float))
                and not isinstance(item, bool)
                for item in data
            )

        return isinstance(data, (int, float)) and not isinstance(data, bool)

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            numeric_strings = [str(item) for item in data]
            self._storage.extend(numeric_strings)
        else:
            self._storage.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)

        return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            self._storage.extend(data)
        else:
            self._storage.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(
                isinstance(log_entry, dict)
                and all(
                    isinstance(key, str)
                    and isinstance(value, str)
                    for key, value in log_entry.items()
                )
                for log_entry in data
            )

        if isinstance(data, dict):
            return all(
                isinstance(key, str)
                and isinstance(value, str)
                for key, value in data.items()
            )

        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, list):
            self._storage.extend(data)
        else:
            self._storage.append(data)


def main():
    print("=== Code Nexus - Data Processor ===")
    print("")

    print("Testing Numeric Processor...")
    num_processor = NumericProcessor()

    num_test_1 = num_processor.validate(42)
    print(f" Trying to validate input '42': {num_test_1}")
    num_test_2 = num_processor.validate("Hello")
    print(f" Trying to validate input 'Hello': {num_test_2}")

    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_processor.ingest("foo")
    except Exception as error:
        print(f" Got exception: {error}")

    numeric_values: list[int | float] = [1, 2, 3, 4, 5]
    print(f" Processing data: {numeric_values}")
    num_processor.ingest(numeric_values)
    i = 3
    print(f" Extracting {i} values...")
    for index in range(i):
        rank, value = num_processor.output()
        print(f" Numeric value {index}: {value}")

    print("")

    print("Testing Text Processor...")
    text_processor = TextProcessor()

    text_test_1 = text_processor.validate(42)
    print(f" Trying to validate input '42': {text_test_1}")

    text_values = ["Hello", "Nexus", "World"]
    print(f" Processing data: {text_values}")
    text_processor.ingest(text_values)
    i = 1
    print(f" Extracting {i} value...")
    for index in range(i):
        rank, value = text_processor.output()
        print(f" Text value {index}: {value}")

    print("")

    print("Testing Log Processor...")
    log_processor = LogProcessor()

    log_test_1 = log_processor.validate("Hello")
    print(f" Trying to validate input 'Hello': {log_test_1}")

    log_test_2 = [
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server"
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!"
        }
    ]

    print(f" Processing data: {log_test_2}")
    i = 2
    print(f" Extracting {i} values...")
    log_processor.ingest(log_test_2)
    for index in range(i):
        rank, value = log_processor.output()

        log_level = value["log_level"]
        log_message = value["log_message"]

        print(f" Log entry {index}: {log_level}: {log_message}")


if __name__ == "__main__":
    main()
