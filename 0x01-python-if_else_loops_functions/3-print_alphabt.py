#!/usr/bin/python3
for letters in range(ord('a'), ord('z') + 1):
    if letters != ord('e') and letters != ord('q'):
        print("{:c}".format(letters), end="")
