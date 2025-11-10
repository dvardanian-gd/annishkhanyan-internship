#!/bin/bash

for cmd in uptime df free; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "Error: '$cmd' not found" >&2
        exit 1
    fi
done


REPORT_FILE="report.txt"

{
  echo "System Report"
  echo "============="
  echo "Date & Time: $(date '+ %Y-%m-%d %H:%M:%S')"
  echo "User: $USER"
  echo "Hostname: $(hostname)"
  echo "Internal IP: $(hostname -I | awk '{print $1}')"
  echo "External IP: $(curl -s ifconfig.me)"
  echo "Linux Distro: $(lsb_release -ds 2>/dev/null)"
  echo "Disk Usage (/) in GB:"
  df -h / | awk 'NR==2 {print "  Used: "$3" / Total: "$2}' # NR==2 for the second line
  echo "Memory (RAM):"
  free -h | awk '/Mem:/ {print "  Used: "$3" / Total: "$2}'
  echo "CPU:"
  echo "  Cores: $(nproc)"
  echo "  Frequency: $(lscpu | grep 'MHz' | awk '{print $3" MHz"}' | head -1)"
} > "$REPORT_FILE" 2>/dev/null

echo "Report saved to $REPORT_FILE"
