from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_FILES = [
    "notebooks/movies_project_starter.ipynb",
    "data/movies_metadata.csv",
    "data/ratings.csv",
    "data/links.csv",
    "data/credits_curated.csv",
    "data/keywords_curated.csv",
    "requirements.txt",
]


def main() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        raise SystemExit("Missing required files:\n" + "\n".join(missing))
    print("PASS: Movies project template files are present.")


if __name__ == "__main__":
    main()
