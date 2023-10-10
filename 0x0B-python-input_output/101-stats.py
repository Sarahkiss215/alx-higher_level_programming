#!/usr/bin/python3
"""Module 101-stats.py"""


def print_stats(size, stat_code):
    """Print accumulated metrics."""
    print("File size: {}".format(size))
    for k in sorted(stat_code):
        print("{}: {}".format(k, stat_code[k]))

if __name__ == "__main__":
    import sys

    size = 0
    stat_code = {}
    valid_code = ['200', '301', '400', '401', '403', '404', '405', '500']
    ct = 0

    try:
        for ln in sys.stdin:
            if ct == 10:
                print_stats(size, stat_code)
                ct = 1
            else:
                ct += 1

            ln = ln.split()

            try:
                size += int(ln[-1])
            except (IndexError, ValueError):
                pass

            try:
                if ln[-2] in valid_code:
                    if stat_code.get(ln[-2], -1) == -1:
                        stat_code[ln[-2]] = 1
                    else:
                        stat_code[ln[-2]] += 1
            except IndexError:
                pass

        print_stats(size, stat_code)

    except KeyboardInterrupt:
        print_stats(size, stat_code)
        raise
