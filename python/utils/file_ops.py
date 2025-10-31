import logging
from pathlib import Path

def setup_logging():
    logs_path = Path(__file__).resolve().parent.parent / "reports"
    logs_path.mkdir(exist_ok=True)
    log_file= logs_path / "audit.log"

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    return logging.getLogger()

def get_paths():
    base= Path(__file__).resolve().parent.parent
    return {
        "data": base / "data.json",
        "reports" : base.parent / "reports",
    }

