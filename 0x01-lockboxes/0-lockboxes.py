#!/usr/bin/python3
""" defining a function that determine a box is open with it's key
or not.
"""


def canUnlockAll(boxes):
    unlocked = set([0])
    keys = [0]
    while keys:
        current_keys = boxes[keys.pop()]
        for key in current_keys:
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                keys.append(key)
    return len(unlocked) == len(boxed)
