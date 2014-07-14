from english.englishCheck import isEnglishWord
from german.germanCheck import isGermanWord
from german.germanCheck import isNewGermanWord
from german.germanCheck import isProperNoun
from pos.postagger import hasSamePartOfSpeech
from knownFalseFriends.knownFalseFriendsChecker import isKnownFalseFriend

def isFalseFriend(word):
    if word.isdigit() or isProperNoun(word):
        return False

    if isKnownFalseFriend(word):
    	return True

    if isGermanWord(word) and isEnglishWord(word):
    	if isNewGermanWord(word):
    		return False
    	return hasSamePartOfSpeech(word)

    #if isGermanWord(word) and not isEnglishWord(word):
    #	return hasSimiliarWords()
    return False
