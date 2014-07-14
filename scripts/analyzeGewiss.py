from falseFriendsChecker.falseFriendsChecker import  isFalseFriend
from falseFriendsChecker.knownFalseFriends.knownFalseFriendsChecker import getSuggestion
from lxml import etree
import os, codecs
from string import punctuation
import datetime

def cleanText(text):
    for c in punctuation:
        text = text.replace(c, " ")
    text = text.lower()
    text = text.replace("  ", " ")
    return text

def createSuggestion(l):
    if l:
        return "[" + l[0] + "=" + l[1] + ", " + l[2] + "=" + l[3] + "]"
    return "[no suggestion available]"

def analyze(dir_input):
    print(str(datetime.datetime.now().time()) +  " start analyze " + dir_input )
    files = os.listdir(dir_input)
    files.sort()

    for file in files:
        xml_text = codecs.open(dir_input + file, "r", "utf-8")
        xml = etree.parse(xml_text)
        for element in xml.iter("event"):
            if element.text == None:
               pass
            sentence = cleanText(element.text)
            for word in sentence.split():
                if isFalseFriend(word):
                    print(word + " " + createSuggestion(getSuggestion(word)))

analyze('../gewiss/DEU_L1_EV/')
