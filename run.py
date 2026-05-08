import argparse
import logging
import time
import numpy as np
import sys

from utils.logger import setup_logger
from utils.config_loader import load_config
from utils.validator import validate_csv
from utils.processor import generate_signals
from utils.metrics import save_metrics, save_error_metrics


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)
    parser.add_argument("--config", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--log-file", required=True)

    args = parser.parse_args()

    setup_logger(args.log_file)

    start_time = time.time()

    logging.info("Job started")

    try:
        # ------------------------
        # Load Config
        # ------------------------
        config = load_config(args.config)

        seed = config["seed"]
        window = config["window"]
        version = config["version"]

        np.random.seed(seed)

        logging.info(
            f"Config validated: seed={seed}, window={window}, version={version}"
        )

        # ------------------------
        # Load Dataset
        # ------------------------
        df = validate_csv(args.input)

        logging.info(f"Rows loaded: {len(df)}")

        # ------------------------
        # Processing
        # ------------------------
        logging.info("Computing rolling mean")

        df = generate_signals(df, window)

        logging.info("Signal generation completed")

        # ------------------------
        # Metrics
        # ------------------------
        signal_rate = float(df["signal"].mean())

        latency_ms = int((time.time() - start_time) * 1000)

        metrics = save_metrics(
            output_path=args.output,
            version=version,
            rows_processed=len(df),
            signal_rate=signal_rate,
            latency_ms=latency_ms,
            seed=seed,
            status="success"
        )

        logging.info(f"Metrics summary: {metrics}")

        logging.info("Job completed successfully")

        print(metrics)

    except Exception as e:
        logging.exception("Job failed")

        save_error_metrics(
            output_path=args.output,
            version="v1",
            error_message=str(e)
        )

        print({
            "version": "v1",
            "status": "error",
            "error_message": str(e)
        })

        sys.exit(1)


if __name__ == "__main__":
    main()