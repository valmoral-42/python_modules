import sys
from importlib import metadata
from typing import Final


DEPENDENCIES: Final[dict[str, str]] = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "matplotlib": "Visualization"}


def get_package_version(package_name: str) -> str | None:
    try:
        return metadata.version(package_name)
    except metadata.PackageNotFoundError:
        return None


def check_dependencies() -> list[str]:
    missing_packages: list[str] = []

    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    for package_name, purpose in DEPENDENCIES.items():
        version = get_package_version(package_name)
        if version is None:
            print(f"[MISSING] {package_name} - {purpose} unavailable")
            missing_packages.append(package_name)
        else:
            print(f"[OK] {package_name} ({version}) - {purpose} ready")

    requests_version = get_package_version("requests")
    if requests_version is not None:
        print(
            f"[OK] requests ({requests_version}) - "
            "Network access ready")

    return missing_packages


def print_install_help() -> None:
    print()
    print("Missing dependencies detected.")
    print("Install with pip:")
    print("pip install -r requirements.txt")
    print("Install with Poetry:")
    print("poetry install")
    print("Run with Poetry environment:")
    print("poetry run python loading.py")


def show_dependency_management_difference() -> None:
    print()
    print("Dependency management comparison:")
    print("- pip uses requirements.txt in the active environment")
    print("- Poetry uses pyproject.toml and manages its own environment")
    print("- pip usually relies on manual environment handling")
    print("- Poetry combines dependency resolution and environment management")


def run_analysis() -> None:
    try:
        import matplotlib.pyplot as plt  # type: ignore
        import numpy as np  # type: ignore
        import pandas as pd  # type: ignore
    except ImportError:
        print_install_help()
        sys.exit(1)

    np.random.seed()

    matrix_signal = np.random.normal(loc=60.0, scale=15.0, size=1000)
    resistance_rate = np.random.uniform(low=10.0, high=95.0, size=1000)
    anomaly_score = np.random.normal(loc=50.0, scale=20.0, size=1000)

    data_frame = pd.DataFrame(
        {
            "matrix_signal": matrix_signal,
            "resistance_rate": resistance_rate,
            "anomaly_score": anomaly_score})

    data_frame["profile"] = pd.cut(
        data_frame["matrix_signal"],
        bins=[0, 45, 75, 120],
        labels=["BluePill", "Potential", "ZionRebel"])

    grouped = (
        data_frame.groupby("profile", observed=False)[
            ["matrix_signal", "resistance_rate", "anomaly_score"]]
        .mean()
        .round(2))

    print()
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    print(grouped)
    print("Generating visualization...")

    axis = grouped.plot(
        kind="bar",
        figsize=(10, 6),
        color=["#abd4b6", "#abcee0", "#d4abb8"])
    axis.set_title("Matrix Data Analysis by Profile")
    axis.set_xlabel("Profile")
    axis.set_ylabel("Average Value")
    axis.grid(axis="y", linestyle="--", alpha=0.3)

    plt.tight_layout()
    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    missing_packages = check_dependencies()
    show_dependency_management_difference()

    if missing_packages:
        print_install_help()
        sys.exit(1)

    run_analysis()


if __name__ == "__main__":
    main()
