#!/usr/bin/python
import os, sys
from falseFriendsMapper import ffmap

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
sys.path.insert(0, location + '/../german')


def isKnownFalseFriend(word):
    for l in ffmap:
        if l[0] == word:
            return True
    return False


def getSuggestion(word):
    for l in ffmap:
        if l[0] == word:
            return (l[0],l[1], l[2], l[3])
    return None
