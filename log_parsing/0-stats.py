#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.

It processes log entries in the format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

After every 10 lines and/or upon keyboard interruption (CTRL + C), it prints:
- Total file size: the sum of all file sizes
- Number of lines for each status code (200, 301, 400, 401, 403, 404, 405, 500)
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
    Print the current statistics: total file size and status code counts.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """
    Handle keyboard interruption (CTRL + C) to print the stats before exiting.
    """
    print_stats()
    sys.exit(0)


# Set up the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1

        try:
            parts = line.split()
            if len(parts) < 9:
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