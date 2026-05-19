import sys


def command() -> None:
    argc = len(sys.argv)
    i = 0
    print(f"Program name: {sys.argv[0]}")
    if len == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received {argc - 1}")
        for i < argc:
            print(f"Argument {i}: {sys.argv[i]}")
            i =+ 1
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    command()
