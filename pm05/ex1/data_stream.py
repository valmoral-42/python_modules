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
                    for key, value in log_entry.items()) for log_entry in data)

        if isinstance(data, dict):
            return all(
                isinstance(key, str)
                and isinstance(value, str)
                for key, value in data.items())
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, list):
            self._storage.extend(data)
        else:
            self._storage.append(data)


class DataStream():
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            processor_found = False
            for processor in self._processors:
                if processor.validate(item):
                    processor.ingest(item)
                    processor_found = True
                    break
            if not processor_found:
                print(f"Data Stream error -"
                      f" Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        for proc in self._processors:
            nm = proc.__class__.__name__.replace("Processor", " Processor")
            total_items = proc._current_rank + len(proc._storage)
            remaining = len(proc._storage)
            print(f"{nm}: total {total_items}"
                  f" items processed, remaining {remaining} on processor")

        if not self._processors:
            print("No processor found, no data")
            print("")


def main():
    print("=== Code Nexus - Data Stream ===")
    print("")

    print("Initialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("Registering Numeric Processor")
    print("")
    numeric_proc = NumericProcessor()
    data_stream.register_processor(numeric_proc)
    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
             'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
        ]

    print(f"Send first batch of data on stream: {batch}")
    data_stream.process_stream(batch)
    data_stream.print_processors_stats()
    print("")

    print("Registering other data processors")
    text_proc = TextProcessor()
    data_stream.register_processor(text_proc)
    log_proc = LogProcessor()
    data_stream.register_processor(log_proc)

    print("Send the same batch again")
    data_stream.process_stream(batch)
    data_stream.print_processors_stats()
    print("")

    print("Consume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        numeric_proc.output()
    for _ in range(2):
        text_proc.output()
    for _ in range(1):
        log_proc.output()
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
