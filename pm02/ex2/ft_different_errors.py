def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    if operation_number == 1:
        _ = 10 / 0
    if operation_number == 2:
        open("non.txt")
    if operation_number == 3:
        _ = "abc" + 1
    if operation_number == 4:
        _ = 25


def test_error_types() -> None:
    nums = [0, 1, 2, 3, 4]

    for num in nums:
        print(f"Testing operation {num}...")
        try:
            garden_operations(num)
            print("Operation completed successfully")
        except (ValueError, ZeroDivisionError, FileNotFoundError,
                TypeError) as e:
            print(f"Caught {type(e).__name__} error: {e}")
    print("")
    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
