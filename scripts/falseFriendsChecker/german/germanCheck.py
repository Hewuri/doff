from pygermanet.germanet import *
import os

gn = load_germanet()


def readFile(file):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f = open(os.path.join(location, file), "r")
    return set([x.lower() for x in set(f.read().splitlines())])

words = readFile("germanWords.txt")
newWords = readFile("newGermanWords.txt")
properNouns = readFile("germanProperNouns.txt")
stopWords = readFile("germanStopWords.txt")

def isGermanWord(word):
    inWordList = word in words
    inGermanNet = (isInGermanaNet(word) or isInGermanaNet(word.capitalize()))
    return inWordList or inGermanNet

def isInGermanaNet(word):  # Case sensitive!
    lemmas = gn.lemmatise(word)
    for lemma in lemmas:
        if gn.synsets(lemma):
            return True
    return False


def isNewGermanWord(word):
    return word in newWords

def isProperNoun(word):
    return word in properNouns

def getPossiblePOS(word):
    parts = set()
    for s in gn.synsets(gn.lemmatise(word)[0]):
        parts.add(s.pos)
    for s in gn.synsets(gn.lemmatise(word.capitalize())[0]):
        parts.add(s.pos)
    return list(parts)

