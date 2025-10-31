#collect_info.ps1
#------------------------
#System Auditor - Data Collector
#This scripts gather system info and saves it as JSON for Python to analyze.
#------------------------

#--- 1. Collect process information ---
$processes = Get-Process | Select-Object Name, Id, CPU, StartTime -ErrorAction SilentlyContinue

#--- 2. Collect service information ---
$services = Get-Service | Select-Object Name, Status, DisplayName

#--- 3. Collect network information ---
$network = Get-NetIPAddress | Select-Object IPAddress, InterfaceAlias, AddressFamily

#--- 4. Collect latest system logs ---
$logs = Get-EventLog -LogName System -Newest 50 | Select-Object TimeGenerated, EntryType, Source, Message

#--- 5. Create the output object ---
$data = @{
    "Timestamp"  = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    "Processes" = $processes
    "Services" = $services
    "Network" = $network
    "Logs" = $logs
}

# --- 6. Convert to JSON and export ---
$outputPath = "..\python\data.json"

$data | ConvertTo-Json -Depth 5 | Out-File $outputPath -Encoding utf8

Write-Host "System data collected and saved to $outputPath"
