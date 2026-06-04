import sys


def text_recovery() -> None:

    argc = len(sys.argv)
    if argc != 2:
        print("Usage: ft_ancient_text.py <file>")
        print("")
        return
    else:
        file_name = sys.argv[1]
        print(f"Accessing file '{file_name}'")

        try:
            vault = open(file_name, "r")
            print("---")
            print("")

            file_content = vault.read()
            print(f"{file_content}")
            print("---")

            vault.close()
            print(f"File '{file_name}' closed.")

        except Exception as e:
            print(f"Error opening file '{file_name}': {e}")
            print("")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    text_recovery()
