#!/usr/bin/env python3
"""
A script to read stdin line by line, compute metrics, and print statistics.

The script tracks:
- Total file size from log entries.
- The number of occurrences of specific HTTP status codes.
"""

import sys
import signal

# Initialize global metrics
total_size = 0
status_codes = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0


def print_stats():
    """
    Print the current statistics of total file size and status code counts.

    This function prints:
    - The total file size so far.
    - The number of occurrences for each status code that has appeared.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """
    Handle keyboard interruption (CTRL + C) to print the stats before exiting.

    Args:
        sig (int): Signal number.
        frame (frame object): The current stack frame.
    """
    print_stats()
    sys.exit(0)


# Set up the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        try:
            global total_size
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

        except (ValueError, IndexError):
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