from src.pipeline import run_pipeline


if __name__ == "__main__":
    result = run_pipeline()
    print("UKCS Field Economics baseline analysis complete")
    for key, value in result.items():
        print(f"{key}: {value}")

