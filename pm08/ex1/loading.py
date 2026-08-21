import sys
from importlib import metadata
from typing import Final


DEPENDENCIES: Final[dict[str, str]] = {
    "numpy": "Numerical computation",
    "pandas": "Data manipulation",
    "matplotlib": "Data visualization"}

SUBJECT_COUNT: Final[int] = 1000

PROFILE_BINS: Final[list[float]] = [
    -0.1,
    30.0,
    60.0,
    75.0,
    100.1]

PROFILE_LABELS: Final[list[str]] = [
    "Dormant",
    "Questioning",
    "Aware",
    "Awakened"]

PROFILE_COLORS: Final[list[str]] = [
    "#2c7194",
    "#97bacc",
    "#cc839d",
    "#942c52"]


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

    return missing_packages


def print_install_help() -> None:
    print()
    print("Missing dependencies detected.")
    print("Install with pip:")
    print("pip install -r requirements.txt")
    print("Install with Poetry:")
    print("poetry install")
    print("Run with Poetry:")
    print("poetry run python loading.py")


def show_dependency_management_difference() -> None:
    print()
    print("Dependency management comparison:")
    print("- pip uses requirements.txt in the active environment")
    print("- Poetry uses pyproject.toml and manages its own environment")


def run_analysis() -> None:
    try:
        import matplotlib.pyplot as plt  # type: ignore
        import numpy as np  # type: ignore
        import pandas as pnd  # type: ignore
    except ImportError:
        print_install_help()
        sys.exit(1)

    matrix_signal = np.clip(
        np.random.normal(loc=5, scale=90, size=SUBJECT_COUNT), 0, 100)

    resistance_rate = np.random.uniform(low=0, high=100, size=SUBJECT_COUNT)

    data_frame = pnd.DataFrame(
        {"matrix_signal": matrix_signal,
         "resistance_rate": resistance_rate})

    data_frame["awakening_score"] = (
        data_frame["matrix_signal"] * 0.6
        + data_frame["resistance_rate"] * 0.4)

    data_frame["profile"] = pnd.cut(
        data_frame["awakening_score"],
        bins=PROFILE_BINS,
        labels=PROFILE_LABELS)

    profile_counts = data_frame["profile"].value_counts(sort=False)

    print()
    print(f"Analyzing {SUBJECT_COUNT} connected subjects...")
    print("Awakening profile distribution:")

    for profile_name, subject_count in profile_counts.items():
        print(f"{str(profile_name):<12} {subject_count}")

    axis = profile_counts.plot(
        kind="bar",
        figsize=(10, 6),
        color=PROFILE_COLORS,
        edgecolor="#000000")

    axis.set_title("Matrix Population", color="#000000", pad=15)
    axis.set_xlabel("Awakening Profile", color="#000000")
    axis.set_ylabel("Connected Subjects", color="#000000")
    axis.grid(axis="y", linestyle="--", alpha=0.35)
    axis.tick_params(axis="x", rotation=0)
    axis.set_facecolor("#FAFAFA")

    plt.tight_layout()
    plt.savefig("matrix_analysis.png", dpi=150)
    plt.close()

    print()
    print("Visualization saved to: matrix_analysis.png")


def main() -> None:
    missing_packages = check_dependencies()
    show_dependency_management_difference()

    if missing_packages:
        print_install_help()
        sys.exit(1)

    run_analysis()


if __name__ == "__main__":
    main()
