import sys


def stream_management() -> None:

    argc = len(sys.argv)
    if argc != 2:
        print("Usage: ft_ancient_text.py <file>")
        print("")
        return

    file_content = []

    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")

    try:
        vault = open(file_name, "r")

        for line in vault:
            file_content.append(line)

        print("---")
        print("")

        for line in file_content:
            print(line.rstrip())
        print("")
        print("---")

        vault.close()
        print(f"File '{file_name}' closed.")
        print("")

    except FileNotFoundError as e:
        print(f"[STDERR] Error opening file '{file_name}': {e}",
              file=sys.stderr)
        print("")
        return

    print("Transform data:")
    print("---")
    print("")

    new_content = []
    for line in file_content:
        temp_line = line.rstrip('\n')
        new_line = f"{temp_line}#"
        new_content.append(new_line)
        print(new_line)
    print("")
    print("---")

    sys.stdout.write("Enter new file name (or empty):")
    sys.stdout.flush()
    new_name = sys.stdin.readline().strip()
    if new_name:
        print(f"Saving data to '{new_name}'")
        try:
            new_file = open(new_name, "w")
            final_content = "\n".join(new_content)
            new_file.write(final_content)
            print(f"Data saved in file '{new_name}'.")
        except Exception as e:
            print(f"[STDERR] Error opening file '{new_name}': {e}",
                  file=sys.stderr)
            print("Data not saved.")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    stream_management()
