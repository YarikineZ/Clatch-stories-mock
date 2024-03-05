from enum import Enum


class AccessLevel(Enum):
    onlyClatchTeam = "onlyClatchTeam"
    allUsers = "allUsers"


class TextPosition(Enum):
    # TODO: Fix
    top = "top"
    allUsers = "allUsers"

class TextAlign(Enum):
    left = "left"
    mid = "middle"
    right = "right"