#!/usr/bin/python3
"""Module for stats"""


def print_stats(file_size, status_codes):
    """Prints the stats of a log"""
    print("File size: {}".format(file_size))
    for k, v in sorted(status_codes.items()):
        print("{}: {}".format(k, v))


def main():
    """Parses the logs"""
    import sys
    import re

    file_size = 0
    status_codes = {}
    try:
        for line in sys.stdin:
            file_size += int(re.match(r".+? (\d+)$", line).group(1))
            status = re.match(r".+? (\d+)$", line).group(1)
            if status in status_codes:
                status_codes[status] += 1
            else:
                status_codes[status] = 1
            if len(status_codes) == 10:
                print_stats(file_size, status_codes)
                status_codes = {}
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise


if __name__ == "__main__":
    main()
