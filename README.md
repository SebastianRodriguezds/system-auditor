# system-auditor
# 🧩 System Auditor (PowerShell + Python)
automation project that collects and analyzes Windows system information using **PowerShell** and **Python**.

# Tool gathers
- Running processes
- Active services
- Network Configuration
- Recent system event logs

Then Python analyzes the data and generates a summary report. 

## Tech Stack
- **PowerShell**: Data collection (processes, services, logs)
- **Python**: Analysis & report generation
- **Pandas** for CSV handling
- **JSON** as the data bridge

## How to Run
powershell powershell -ExecutionPolicy Bypass -File .\powershell\collect_info.ps1 Run Python analyzer: python .\python\analyze_data.py
Find reports in /reports/.

## Future Improvements
Export to HTML dashboard
Email reports
SQLite history for trend analysis
Web dashboard (Flask)