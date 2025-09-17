#!/usr/bin/env python3
import sys

def count_errors(filename: str) -> int:
    """
    Count how many lines contain the substring 'ERROR'.
    Uses a simple, memory-efficient line-by-line scan.
    """
    count = 0
    with open(filename, "r", encoding="utf-8") as f:  # 'f' is just a variable name for the file handle
        for line in f:                                # iterate line by line
            if "ERROR" in line:                       # substring check
                count += 1
    return count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 count_errors.py <path-to-logfile>")
        sys.exit(1)

    path = sys.argv[1]
    print(count_errors(path))
