#!/usr/bin/python3
"""Lockboxes"""


class Keys:
    """keys class"""

    def __init__(self, numOfBoxes: int):
        """init function"""
        self.keys: dict = {}
        for i in range(numOfBoxes):
            self.keys[f'{i}'] = True if i == 0 else False


class Boxes:
    """boxes info class"""
    Locked = []


class Box:
    """box class"""

    def __init__(self, keysList: list, idx: int, k: Keys):
        """init function"""
        self._k = k
        self._keysList = keysList
        self._idx = idx
        if str(idx) in k.keys and k.keys[str(idx)] == True:
            for key in keysList:
                k.keys[str(key)] = True
        else:
            Boxes.Locked.append(self)

    def update(self):
        """update function"""
        if str(self._idx) in self._k.keys and self._k.keys[str(self._idx)] == True:
            for key in self._keysList:
                self._k.keys[str(key)] = True


def canUnlockAll(boxes):
    """canUnlockAll function"""
    l = len(boxes)
    k = Keys(l)
    for i in range(l):
        Box(boxes[i], i, k)
    for box in Boxes.Locked:
        box.update()
    for val in k.keys.values():
        if not val:
            return False
    return True
