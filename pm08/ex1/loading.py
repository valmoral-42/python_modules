import sys
import importlib.metadata


def check_packages() -> None:
    dependencies: dict[str, str] = {
        "pandas": "Data manipulation",
        "numpy": "Numerical computation",
        "matplotlib": "Visualization",
    }

    print("Checking dependencies:")

    missing_packages = []

    for lib, function in dependencies.items():
        try:
            version = importlib.metadata.version(lib)
            print(f"[OK] {lib} ({version}) - {function} ready")
        except ImportError:
            print(f"[MISSING] {lib} - Required for: {function}")
            missing_packages.append(lib)

    if missing_packages:
        print("\nMissing dependencies. To install run:")
        print("To use pip: pip install -r requirements.txt")
        print("To use poetry: poetry install")

        sys.exit(1)


def make_matrix_from_data() -> None:
    try:
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt

        np.random.seed(42)
        ids = np.arange(1001, 2001)
        hack_level = np.random.normal(
            loc=60, scale=15, size=1000
        )
        return_rate = np.random.uniform(
            low=5, high=95, size=1000
        )
        df = pd.DataFrame(
            {
                "ID": ids,
                "Hack_level": hack_level,
                "Return_rate": return_rate,
            }
        )

        print("\nAnalyzing Matrix data...")
        df["Category"] = pd.cut(
            df["Hack_level"],
            bins=[0, 45, 75, 120],
            labels=["BluePill", "Potencial", "ZionRebel"]
        )

        resumen = df.groupby("Category", observed=False).mean()
        print(resumen)

        print()
        print("Generating visulization...")
        print()
        resumen[["Hack_level", "Return_rate"]].plot(
            kind="bar", color=["#BCA0CA", "#7213B1"], figsize=(8, 5))
        plt.title("Matrix Diagnostics: Hack Level & Return Rate by Category")
        plt.ylabel("Rate medium")
        plt.xlabel("Subject category")
        plt.xticks(rotation=0)
        plt.grid(axis="y", linestyle="--", alpha=0.3)
        plt.tight_layout()
        graphic_name = "matrix_graphic.png"
        plt.savefig(graphic_name)
        plt.close()

        print("Analysis complete!")
        print("Result saved to: matrix_graphic.png")

    except Exception as error:
        print(f"{error}")
        return


def loading() -> None:
    print()
    print("LOADING STATUS: Loading programs...")
    print()
    check_packages()
    make_matrix_from_data()


if __name__ == "__main__":
    loading()
