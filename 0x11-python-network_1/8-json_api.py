#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import sys
import requests


if __name__ == "__main__":
    l = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": l}

    i = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        resp = i.json()
        if resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp.get("id"), resp.get("name")))
    except ValueError:
        print("Not a valid JSON")
