#!/usr/bin/python
#
# Checks for a trello link in the ticket
import re
import sys


def main():
    f = open(sys.argv[1], "r")
    commit_msg = f.read()
    f.close()

    found = re.search('https://trello.com', commit_msg)

    if not found:
        sys.exit(1)
    else:
        sys.exit(0)
