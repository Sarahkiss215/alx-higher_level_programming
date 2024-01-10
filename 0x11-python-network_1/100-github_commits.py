#!/usr/bin/python3
"""Python script that takes 2 arguments in order to solve this challenge.
"""

import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    i = requests.get(url)
    cmmts = i.json()
    try:
        for j in range(10):
            print("{}: {}".format(
                cmmts[j].get("sha"),
                cmmts[j].get("commit").get("author").get("name")))
    except IndexError:
        pass
