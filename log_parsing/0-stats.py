#!/usr/bin/env python3
import sys
import signal

# Initialize metrics
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Function to print the current statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Handles the keyboard interruption (CTRL + C) and prints the stats before exiting"""
    print_stats()
    sys.exit(0)

# Set up the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        try:
            parts = line.split()
            if len(parts) < 7:
                continue  # Skip malformed lines

            # Extract file size and status code
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            # Update the total file size
            total_size += file_size

            # Update status code count if it's a valid code
            if status_code in status_codes:
                status_codes[status_code] += 1

        except Exception:
            continue  # Skip lines with parsing errors

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

    # Print final stats at the end of the input
    print_stats()

except KeyboardInterrupt:
    # Catch keyboard interrupt and print stats before exiting
    print_stats()
    sys.exit(0)