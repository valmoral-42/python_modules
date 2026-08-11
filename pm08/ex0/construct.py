import os
import site
import sys


def in_virtual_environment() -> bool:
    return sys.prefix != getattr(sys, "base_prefix", sys.prefix)


def get_environment_name() -> str:
    virtual_env = os.environ.get("VIRTUAL_ENV")
    if virtual_env:
        return os.path.basename(virtual_env)
    return os.path.basename(sys.prefix)


def get_package_path() -> str:
    site_packages = site.getsitepackages()
    if site_packages:
        return site_packages[0]
    user_site = site.getusersitepackages()
    return user_site


def main() -> None:
    print("MATRIX STATUS:", end=" ")

    if in_virtual_environment():
        print("Welcome to the construct")
        print()

        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {get_environment_name()}")
        print(f"Environment Path: {sys.prefix}")
        print()

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print()

        print(f"Package installation path: {get_package_path()}")
    else:
        print("You're still plugged in")
        print()

        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()

        print(f"Global package installation path: {get_package_path()}")
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print(r"matrix_env\Scripts\activate     # On Windows")
        print()

        print("Then run this program again.")


if __name__ == "__main__":
    print()
    main()
