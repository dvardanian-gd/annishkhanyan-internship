#!/bin/bash

# Check if required commands exist
for cmd in uptime df free hostname curl lsb_release nproc lscpu; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "Error: '$cmd' not found" >&2
        exit 1
    fi
done

REPORT_FILE="report.txt"

{
  echo "System Report"
  echo "============="
  echo "Date & Time: $(date '+%Y-%m-%d %H:%M:%S')"
  echo "User: $USER"
  echo "Hostname: $(hostname)"
  echo "Internal IP: $(hostname -I | awk '{print $1}')"
  echo "External IP: $(curl -s ifconfig.me)"
  echo "Linux Distro: $(lsb_release -ds 2>/dev/null)"
  echo
  echo "System Uptime:"
  uptime -p
  echo
  echo "Disk Space (/) in GB:"
  df -h / | awk 'NR==2 {print "  Used: "$3" / Total: "$2" (Free: "$4")"}'
  echo
  echo "Memory (RAM):"
  free -h | awk '/Mem:/ {print "  Total: "$2", Free: "$4}'
  echo
  echo "CPU:"
  echo "  Cores: $(nproc)"
  echo "  Frequency: $(lscpu | awk -F: "/MHz/ {print \$2\" MHz\"; exit}")"
} > "$REPORT_FILE" 2>/dev/null

echo "Report saved to $REPORT_FILE"
