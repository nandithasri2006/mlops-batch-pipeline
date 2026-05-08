import os
import pandas as pd


def validate_csv(input_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError("Input CSV file not found")

    if os.path.getsize(input_path) == 0:
        raise ValueError("Input CSV file is empty")

    try:
        # Read malformed CSV safely
        df = pd.read_csv(
            input_path,
            quotechar='"',
            skipinitialspace=True
        )

        # If entire row became one column, split manually
        if len(df.columns) == 1:
            df = pd.read_csv(
                input_path,
                sep=",",
                quotechar='"',
                engine="python"
            )

    except Exception as e:
        raise ValueError(f"Invalid CSV format: {str(e)}")

    # Convert columns to lowercase
    df.columns = df.columns.str.lower()

    if "close" not in df.columns:
        raise ValueError("Missing required column: close")

    if len(df) == 0:
        raise ValueError("Dataset has no rows")

    return df