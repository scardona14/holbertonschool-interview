#!/usr/bin/python3

""" Lockboxes """

def canUnlockAll(boxes):
    """
    - boxes is a list of lists
    - A key with the same number as a box opens that box
    - You can assume all keys will be positive integers
    - The first box boxes[0] is unlocked
    - Return True if all boxes can be opened, else return False
    """

    canUnlockAll = False
    keys = [0]
    visited = set()

    while keys:
        box = keys.pop(0)
        visited.add(box)

        for key in boxes[box]:
            if key not in visited and key < len(boxes):
                keys.append(key)

    if len(visited) == len(boxes):
        canUnlockAll = True

    return canUnlockAll
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
        if len(keys) == len(boxes):
            canUnlockAll = True
        return canUnlockAll