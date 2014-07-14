from nltk.corpus import wordnet

def isEnglishWord(word):
	return wordnet.synsets(word)
