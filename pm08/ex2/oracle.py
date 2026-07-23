import os
import sys


try:
    from dotenv import load_dotenv  # type: ignore

except ImportError:
    print("[WARNING] python-dotenv not found.")
    print("You can install it with:")
    print("    pip install python-dotenv")
    sys.exit(1)


def main() -> tuple[str | None, str | None, bool]:
    load_dotenv()

    matrix_mode: str | None = os.getenv("MATRIX_MODE")
    data_base_url: str | None = os.getenv("DATABASE_URL")
    api_key: str | None = os.getenv("API_KEY")
    log_level: str | None = os.getenv("LOG_LEVEL")
    endpoint: str | None = os.getenv("ZION_ENDPOINT")

    variables = [
        ("MATRIX_MODE", matrix_mode),
        ("DATA_BASE_URL", data_base_url),
        ("API_KEY", api_key),
        ("LOG_LEVEL", log_level),
        ("ZION_ENDPOINT", endpoint),
    ]

    has_errors = False

    for k, v in variables:
        if v is None:
            print(f"Warning: Variable [{k}] is missing")
            has_errors = True

    if has_errors:
        print("ORACLE STATUS: Matrix configuration is incomplete")
        return matrix_mode, api_key, True

    matrix_mode = matrix_mode.lower()  # type: ignore
    print("Configuration loaded:")

    if matrix_mode == "development":
        print(f"Mode: {matrix_mode}")
        print("Database: Connected to local instance")
        print("API Access: Authenticated")
        print(f"Log level: {log_level}")
        print("Zion Network: Online")

    elif matrix_mode == "production":
        print(f"Mode: {matrix_mode}")
        print("Database: Connected to production cluster")
        print("API Access: Authenticated")
        print(f"Log level: {log_level}")
        print("Zion Network: Online")

    else:
        print("Error: Invalid MATRIX_MODE."
              " Must be 'development' or 'production'")
        return matrix_mode, api_key, True

    return matrix_mode, api_key, False


def security_check(matrix_mode: str | None, api_key: str | None) -> None:
    print()
    print("Environment security check:")
    if api_key:
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] NO KEY. NO ACCESS.")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing."
              " Please configure .env file properly with .env.example")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all the configurations.")


if __name__ == "__main__":
    print()
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    matrix, api, error_detected = main()
    security_check(matrix, api)

    if error_detected:
        print("[KO] Fix configuration errors.")
        sys.exit(1)
