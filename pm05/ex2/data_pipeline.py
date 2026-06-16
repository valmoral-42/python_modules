from abc import ABC, abstractmethod
from typing import Any, Protocol


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

    def output(self) -> tuple[int, str]:
        if not self._storage:
            return (0, "")

        output_data = self._storage.pop(0)
        real_rank = self._current_rank
        self._current_rank += 1
        return (real_rank, output_data)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(
                isinstance(item, (int, float))
                and not isinstance(item, bool)
                for item in data)
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
                    for key, value in
                    log_entry.items()) for log_entry in data)

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
            for log_entry in data:
                formatted_log = (
                    f"{log_entry['log_level']}: "
                    f"{log_entry['log_message']}"
                )
                self._storage.append(formatted_log)
        else:
            formatted_log = f"{data['log_level']}: {data['log_message']}"
            self._storage.append(formatted_log)


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


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
                print("Data Stream error -"
                      f" Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        for proc in self._processors:
            nm = proc.__class__.__name__.replace("Processor", " Processor")
            total_items = proc._current_rank + len(proc._storage)
            remaining = len(proc._storage)
            print(f"{nm}: total {total_items} items processed,"
                  f" remaining {remaining} on processor")

        if not self._processors:
            print("No processor found, no data")
            print("")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            collected_data = []
            i = 0

            while i < nb and len(proc._storage) > 0:
                data = proc.output()
                if data != (0, ""):
                    collected_data.append(data)
                i += 1

            if collected_data:
                plugin.process_output(collected_data)


class CSVExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")

        if not data:
            print("")
            return

        print(",".join(text for _, text in data))


class JSONExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")

        if not data:
            print("{}")
            return

        lines_json = []
        for rank, text in data:
            clean_line = text.strip("\n")
            line_with_data = f'"item_{rank}": "{clean_line}"'
            lines_json.append(line_with_data)
        united_data = ", ".join(lines_json)
        json_final = "{" + united_data + "}"
        print(json_final)


def main():
    print("=== Code Nexus - Data Pipeline ===")
    print("")

    print("Initialize Data Stream...")
    print("")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("Registering Processors")
    print("")
    numeric_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    data_stream.register_processor(numeric_proc)
    data_stream.register_processor(text_proc)
    data_stream.register_processor(log_proc)

    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
             'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']]

    print(f"Send first batch of data on stream: {batch}")
    data_stream.process_stream(batch)
    print("")
    data_stream.print_processors_stats()

    print("")
    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    data_stream.output_pipeline(nb=3, plugin=csv_plugin)
    print("")

    data_stream.print_processors_stats()

    batch2 = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
              [{'log_level': 'ERROR', 'log_message': '500 server crash'},
               {'log_level': 'NOTICE', 'log_message': 'Certificate expires'
               ' in 10 days'}], [32, 42, 64, 84, 128, 168], 'World hello']
    print("")
    print(f"Send another batch of data: {batch2}")
    data_stream.process_stream(batch2)
    print("")
    data_stream.print_processors_stats()
    print("")

    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    data_stream.output_pipeline(nb=5, plugin=json_plugin)
    print("")
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
