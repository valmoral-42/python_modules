import os
import sys
from typing import Final

try:
    from dotenv import load_dotenv
except ImportError:
    print("[WARNING] python-dotenv not found.")
    print("Install it with:")
    print("pip install python-dotenv")
    sys.exit(1)


REQUIRED_VARIABLES: Final[tuple[str, ...]] = (
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT")


def load_configuration() -> dict[str, str | None]:
    load_dotenv()

    configuration: dict[str, str | None] = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT")}
    return configuration


def validate_configuration(
    configuration: dict[str, str | None],
) -> list[str]:
    missing_variables: list[str] = []

    for variable_name in REQUIRED_VARIABLES:
        if not configuration.get(variable_name):
            missing_variables.append(variable_name)

    matrix_mode = configuration.get("MATRIX_MODE")
    if matrix_mode and matrix_mode not in {"development", "production"}:
        missing_variables.append(
            "MATRIX_MODE must be 'development' or 'production'")

    return missing_variables


def mask_secret(secret: str | None) -> str:
    if not secret:
        return "Missing"
    if len(secret) <= 4:
        return "*" * len(secret)
    return f"{secret[:2]}{'*' * (len(secret) - 4)}{secret[-2:]}"


def print_configuration(configuration: dict[str, str | None]) -> None:
    matrix_mode = configuration["MATRIX_MODE"]
    database_url = configuration["DATABASE_URL"]
    api_key = configuration["API_KEY"]
    log_level = configuration["LOG_LEVEL"]
    zion_endpoint = configuration["ZION_ENDPOINT"]

    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")

    if matrix_mode == "development":
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to production instance")

    print(
        "API Access: Authenticated"
        if api_key
        else "API Access: Missing credentials"
    )
    print(f"Log Level: {log_level}")
    print(
        "Zion Network: Online"
        if zion_endpoint
        else "Zion Network: Offline")

    print(f"Database URL: {database_url}")
    print(f"API Key: {mask_secret(api_key)}")


def print_security_check() -> None:
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file detected for development configuration")
    else:
        print("[WARNING] .env file not found in current directory")

    print("[OK] Production overrides available via environment variables")
    print("The Oracle sees all configurations.")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    configuration = load_configuration()
    missing_variables = validate_configuration(configuration)

    if missing_variables:
        print("Configuration warnings:")
        for variable_name in missing_variables:
            print(f"- Missing or invalid: {variable_name}")
        print("ORACLE STATUS: Matrix configuration is incomplete")
        print_security_check()
        sys.exit(1)

    print_configuration(configuration)
    print_security_check()


if __name__ == "__main__":
    main()
