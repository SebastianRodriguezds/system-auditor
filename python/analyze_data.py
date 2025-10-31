import json
import pandas as pd
from datetime import datetime
from pathlib import Path

from utils.file_ops import setup_logging, get_paths

log = setup_logging()
paths = get_paths()

#Locate and load data
base_path = Path(__file__).resolve().parent
date_path = paths["data"]
reports_path = paths["reports"]

if not date_path.exists():
    raise FileNotFoundError(f"Data file not found: {date_path}")

with open(date_path, "r", encoding="utf-8-sig") as f:
    data = json.load(f)

print("Data loaded successfully")
log.info(f"Loaded data from {paths['data']}")

# --- 2. Analyze the system data
log.info("Starting system audit analysis...")
# Find services that are not runninf
stopped_serv = [svc for svc in data["Services"] if svc["Status"] != "Running"]

# top 5 process by CPU usage
processes = [p for p in data["Processes"] if "CPU" in p and p["CPU"] is not None]
top_processes = sorted(processes, key=lambda x: x["CPU"], reverse=True)[:5]

# Count log entries by type (Error, Warning, Information)
log_counts = {}
type_map = {1: "Error", 3: "Warning", 4: "Information"}

for log_entry in data["Logs"]:
    entry_value = log_entry.get("EntryType", None)
    entry_type = type_map.get(entry_value, "Unknown")
    log_counts[entry_type] = log_counts.get(entry_type, 0) + 1

# 3 Generate a report 
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

summary_data = {
    "Timestamp" : [data["Timestamp"]],
    "Stopped_Services" : [len(stopped_serv)],
    "Top_CPU_processes" : [", ".join(p["Name"] for p in top_processes)],
    "Logs_Error" : [log_counts.get("Error",0)],
    "Logs_Warning" : [log_counts.get("Warning",0)],
    "Logs_Info" : [log_counts.get("Information",0)],
}



summary_df = pd.DataFrame(summary_data)

#sabe it
output_file = reports_path / f"report_{timestamp}.csv"
summary_df.to_csv(output_file, index=False)

log.info(f"Generated report: {output_file}")