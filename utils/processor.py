import numpy as np


def generate_signals(df, window):
    df["rolling_mean"] = df["close"].rolling(window=window).mean()

    df["signal"] = np.where(
        df["close"] > df["rolling_mean"],
        1,
        0
    )

    return df