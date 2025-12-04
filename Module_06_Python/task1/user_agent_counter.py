#!/usr/bin/env python3
"""
Script to count User-Agent strings inside a compressed access.log.gz file.
"""

import os
import gzip
import sys
import re
from collections import Counter

def open_log_file(file_path):
    """Opens either a gzip-compressed file or a normal text file."""
    if file_path.endswith(".gz"):
        return gzip.open(file_path, 'rt', encoding='utf-8', errors='ignore')
    return open(file_path, 'r', encoding='utf-8', errors='ignore')

def user_agent_counter(file_path):
    """Reads a .gz access log and counts unique User-Agent strings."""
    if not os.path.isfile(file_path):
        print("Path is not valid")
        return

    user_agents = []

    with open_log_file(file_path) as f:  # open gzip file in text mode
        for line in f:
            match = re.search(r'"([^"]*)"$', line)  # the last quoted string in the line
            if match:
                ua = match.group(1).strip()
                if ua:
                    user_agents.append(ua)

    counts = Counter(user_agents)

    print(f"Total number of unique User Agents: {len(counts)}\n")
    for agent, num in counts.items():
        print(f"{agent} : {num}")

def main():
    """Parses command-line arguments and runs the counter."""
    if len(sys.argv) != 2:
        print("Usage: python3 2_user_agent_counter.py <access.log.gz>")
        sys.exit(1)

    file_path = sys.argv[1]
    user_agent_counter(file_path)

if __name__ == "__main__":
    main()
