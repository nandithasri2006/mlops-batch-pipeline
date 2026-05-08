# MLOps Batch Pipeline Task

## Overview

This project is a minimal MLOps-style batch processing pipeline built using Python.

The application:

- Loads configuration from a YAML file
- Reads OHLCV market data from a CSV file
- Computes rolling mean on the `close` column
- Generates binary trading signals
- Produces structured metrics in JSON format
- Creates detailed execution logs
- Runs locally and inside Docker

---

## Project Structure

```text
mlops-task/
│
├── .gitignore
├── run.py
├── config.yaml
├── data.csv
├── requirements.txt
├── Dockerfile
├── README.md
├── metrics.json
├── run.log
│
└── utils/
    ├── __init__.py
    ├── config_loader.py
    ├── validator.py
    ├── processor.py
    ├── metrics.py
    └── logger.py
```

---

## Requirements

- Python 3.9+
- Docker Desktop

---

## Installation

### Clone Repository

```bash
git clone https://github.com/nandithasri2006/mlops-batch-pipeline.git
cd mlops-batch-pipeline
```

### Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Example `config.yaml`

```yaml
seed: 42
window: 5
version: "v1"
```

---

## Running the Application

### Local Execution

```bash
python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log
```

---

## Processing Workflow

1. Load and validate configuration
2. Load and validate dataset
3. Validate required `close` column
4. Compute rolling mean
5. Generate binary signals
6. Compute metrics
7. Write metrics JSON
8. Generate logs

---

## Signal Logic

Rolling mean calculation:

```python
rolling_mean = close.rolling(window=window).mean()
```

Signal generation:

```python
signal = 1 if close > rolling_mean else 0
```

---

## Example Success Output

### metrics.json

```json
{
  "version": "v1",
  "rows_processed": 10000,
  "metric": "signal_rate",
  "value": 0.4989,
  "latency_ms": 95,
  "seed": 42,
  "status": "success"
}
```

---

## Example Error Output

```json
{
  "version": "v1",
  "status": "error",
  "error_message": "Missing required column: close"
}
```

---

## Logging

The application generates logs in:

```text
run.log
```

Logs include:

- Job start timestamp
- Configuration validation
- Dataset loading
- Rolling mean processing
- Signal generation
- Metrics summary
- Error details
- Job completion status

---

## Docker Support

### Build Docker Image

```bash
docker build -t mlops-task .
```

### Run Docker Container

```bash
docker run --rm mlops-task
```

---

## Error Handling

The application handles:

- Missing input files
- Invalid CSV format
- Empty datasets
- Missing required columns
- Invalid configuration structure
- Runtime exceptions

Metrics JSON is generated for both success and failure cases.

---

## Technologies Used

- Python
- Pandas
- NumPy
- PyYAML
- Docker
- Python Logging

---

## Author

Nandhitha Maraka
