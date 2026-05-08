import json


def save_metrics(
    output_path,
    version,
    rows_processed,
    signal_rate,
    latency_ms,
    seed,
    status
):
    metrics = {
        "version": version,
        "rows_processed": rows_processed,
        "metric": "signal_rate",
        "value": round(signal_rate, 4),
        "latency_ms": latency_ms,
        "seed": seed,
        "status": status
    }

    with open(output_path, "w") as f:
        json.dump(metrics, f, indent=2)

    return metrics


def save_error_metrics(output_path, version, error_message):
    error_metrics = {
        "version": version,
        "status": "error",
        "error_message": error_message
    }

    with open(output_path, "w") as f:
        json.dump(error_metrics, f, indent=2)