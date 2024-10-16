#!/usr/bin/python3
import sys

total_size = 0
status_codes = {}

for i, line in enumerate(sys.stdin):
    try:
        _, _, _, _, _, status_code, file_size = line.split()
        status_code = int(status_code)
        file_size = int(file_size)
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1
    except ValueError:
        continue

    if (i + 1) % 10 == 0 or i == 9:
        print(f"Total file size: {total_size}")
        for code in sorted(status_codes.keys()):
            print(f"{code}: {status_codes[code]}")

try:
    while True:
        line = sys.stdin.readline()
        if not line:
            break
except KeyboardInterrupt:
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")