#!/usr/bin/python
import os, sys
from posmap import posmap
from nltk.corpus import treebank
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
sys.path.insert(0, location + '/../german')
from germanCheck import getPossiblePOS


def createPOSList():
    pos_map = dict()
    for a in treebank.tagged_words():
        word = a[0]
        if word not in pos_map:
            pos_map[word] = [posmap[a[1]]]
        else:
            pos_map[word] = list(set(list(posmap[a[1]]) + list(pos_map[word])))
    return pos_map
pos_list_eng = createPOSList()

def getPossiblePartsOfSpeech(word):
    if word in pos_list_eng:
        return list(pos_list_eng[word])
    else:
        return list()

def hasSamePartOfSpeech(word):
    possible_pos_eng = getPossiblePartsOfSpeech(word)
    possible_pos_ger = getPossiblePOS(word)
    if possible_pos_eng and possible_pos_ger:
        for pos in possible_pos_ger:
            if pos in possible_pos_eng:
                return True
    return False
