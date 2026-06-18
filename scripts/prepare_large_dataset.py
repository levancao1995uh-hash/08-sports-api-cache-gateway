import argparse
        from pathlib import Path

        parser = argparse.ArgumentParser(description="Prepare optional large local dataset after explicit user confirmation.")
        parser.add_argument("--target-mb", type=int, default=300)
        args = parser.parse_args()
        out = Path("data/processed/LARGE_DATASET_PLACEHOLDER.txt")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            "This project is configured for a large dataset target of " + str(args.target_mb) +
            " MB. Real data download or generation should be executed only after confirming disk usage, API credentials, and source terms.
",
            encoding="utf-8",
        )
        print(out)
