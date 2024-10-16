#!/usr/bin/python3
import sys

def main():
    total_size = 0
    status_codes = {}

    for i, line in enumerate(sys.stdin):
        try:
            # Split the line into components
            _, _, _, _, _, status_code, file_size = line.split()
            status_code = int(status_code)
            file_size = int(file_size)
            total_size += file_size
            
            # Update status code counts
            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1
        except ValueError:
            continue

        # Print statistics every 10 lines
        if (i + 1) % 10 == 0 or i == 9:
            print(f"Total file size: {total_size}")
            for code in sorted(status_codes.keys()):
                print(f"{code}: {status_codes[code]}")

    try:
        # Keep reading until EOF or KeyboardInterrupt
        while True:
            line = sys.stdin.readline()
            if not line:
                break
    except KeyboardInterrupt:
        # Print final statistics on interrupt
        print(f"Total file size: {total_size}")
        for code in sorted(status_codes.keys()):
            print(f"{code}: {status_codes[code]}")

if __name__ == "__main__":
    main()