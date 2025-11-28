#!/usr/bin/env python3
"""
Simple system information script using psutil and platform.
"""

import argparse
import platform
import getpass
import os
import socket
import psutil


def get_distro_info():
    """Print basic OS and hardware information."""
    print("=== Distro Info ===")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print()


def get_memory_info():
    """Print memory usage information."""
    mem = psutil.virtual_memory()
    print("=== Memory Info ===")
    print(f"Total: {mem.total / (1024 ** 3):.2f} GB")
    print(f"Used: {mem.used / (1024 ** 3):.2f} GB")
    print(f"Free: {mem.available / (1024 ** 3):.2f} GB")
    print()


def get_cpu_info():
    """Print CPU core count and frequencies."""
    print("=== CPU Info ===")
    print(f"Cores (physical): {psutil.cpu_count(logical=False)}")
    print(f"Cores (logical): {psutil.cpu_count(logical=True)}")

    freq = psutil.cpu_freq()
    if freq:
        print(f"Max Frequency: {freq.max:.2f} MHz")
        print(f"Current Frequency: {freq.current:.2f} MHz")
    else:
        print("CPU frequency info not available.")
    print()


def get_user_info():
    """Print current user information."""
    print("=== Current User ===")
    print(f"Username: {getpass.getuser()}")
    print(f"Home Directory: {os.path.expanduser('~')}")
    print()


def get_load_average():
    """Print system load averages."""
    print("=== Load Average (1, 5, 15 min) ===")
    if hasattr(os, "getloadavg"):
        load1, load5, load15 = os.getloadavg()
        print(f"1 min: {load1}, 5 min: {load5}, 15 min: {load15}")
    else:
        print("Load average not supported on this OS")
    print()


def get_ip_address():
    """Print system hostname and IP address."""
    print("=== IP Address ===")
    hostname = socket.gethostname()
    try:
        ip = socket.gethostbyname(hostname)
        print(f"Hostname: {hostname}")
        print(f"IP Address: {ip}")
    except socket.error:
        print("Could not get IP address")
    print()


def main():
    """Parse arguments and display the selected system information."""
    parser = argparse.ArgumentParser(description="Get system information")
    parser.add_argument("-d", "--distro", action="store_true", help="Show distro info")
    parser.add_argument("-m", "--memory", action="store_true", help="Show memory info")
    parser.add_argument("-c", "--cpu", action="store_true", help="Show CPU info")
    parser.add_argument("-u", "--user", action="store_true", help="Show current user info")
    parser.add_argument("-l", "--load", action="store_true", help="Show load average")
    parser.add_argument("-i", "--ip", action="store_true", help="Show IP address")

    args = parser.parse_args()

    # If no arguments provided, show all info
    if not any(vars(args).values()):
        args.distro = args.memory = args.cpu = args.user = args.load = args.ip = True

    if args.distro:
        get_distro_info()
    if args.memory:
        get_memory_info()
    if args.cpu:
        get_cpu_info()
    if args.user:
        get_user_info()
    if args.load:
        get_load_average()
    if args.ip:
        get_ip_address()


if __name__ == "__main__":
    main()
