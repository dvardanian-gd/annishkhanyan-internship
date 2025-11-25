#!/usr/bin/env python3
"""
Script to count User-Agent strings inside a compressed access.log.gz file.
"""

import os
import gzip
import sys
import re
from collections import Counter

def user_agent_counter(file_path):
    """Reads a .gz access log and counts unique User-Agent strings."""
    if not os.path.isfile(file_path):
        print("Path is not valid")
        return

    user_agents = []

    # Open gzip file in text mode
    with gzip.open(file_path, 'rt', encoding='utf-8', errors='ignore') as f:
        for line in f:
            # User-Agent is typically the last quoted string in the line
            match = re.search(r'"([^"]*)"$', line)
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
