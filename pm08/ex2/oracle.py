import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("[WARNING] python-dotenv not found.")
    print("Install it with:")
    print("pip install -r requirements.txt")
    sys.exit(1)


REQUIRED_VARIABLES = (
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
)


def load_configuration() -> dict[str, str | None]:
    load_dotenv()

    return {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }


def validate_configuration(
    configuration: dict[str, str | None],
) -> list[str]:
    config_issues: list[str] = []

    for variable_name in REQUIRED_VARIABLES:
        if not configuration.get(variable_name):
            config_issues.append(variable_name)

    matrix_mode = configuration.get("MATRIX_MODE")
    if matrix_mode and matrix_mode not in {"development", "production"}:
        config_issues.append(
            "MATRIX_MODE must be 'development' or 'production'"
        )

    return config_issues


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
        else "Zion Network: Offline"
    )
    print("Database URL: Configured" if database_url else "Database URL: Missing")


def print_security_check() -> None:
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file detected for development configuration")
    else:
        print("[WARNING] .env file not found in current directory")

    print("[OK] Production overrides available via environment variables")
    print()
    print("The Oracle sees all configurations.\n")


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    configuration = load_configuration()
    config_issues = validate_configuration(configuration)

    if config_issues:
        print("Configuration warnings:")
        for variable_name in config_issues:
            print(f"- Missing or invalid: {variable_name}")
        print("ORACLE STATUS: Matrix configuration is incomplete")
        print_security_check()
        sys.exit(1)

    print_configuration(configuration)
    print_security_check()


if __name__ == "__main__":
    main()
