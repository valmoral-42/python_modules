def secure_archive(file: str, option: str,
                   content: str | None = None) -> tuple[bool, str]:

    try:
        with open(file, option) as test_file:
            if option == 'r':
                content = test_file.read()
                return (True, content)

            elif option == 'w':
                if content is not None:
                    text_to_add = content
                else:
                    text_to_add = "No text provided"
                test_file.write(text_to_add)
                return (True, "Content successfully written to file")

            else:
                return (False, "Unsupported file action.")

    except Exception as error:
        return (False, f"{error}")


def vault_security() -> None:
    print("=== Cyber Archives Security ===")
    print("")

    print("Using 'security_archive' to read from a nonexistent file:")
    test1 = secure_archive("/not/existing/file", "r")
    print(test1)
    print("")

    print("Using 'security_archive' to read from an inaccessible file:")
    test2 = secure_archive("/etc/shadow", "r")
    print(test2)
    print("")

    print("Using 'security_archive' to read from a regular file:")
    test3 = secure_archive("ancient_fragment.txt", "r")
    print(test3)
    print("")

    print("Using 'security_archive' to write previous to a new file:")
    test4 = secure_archive("ancient_fragment.txt", 'w',
                           "toy cansado jefe")
    print(test4)


if __name__ == "__main__":
    vault_security()
