from falseFriendsChecker.falseFriendsChecker import  isFalseFriend
from falseFriendsChecker.knownFalseFriends.knownFalseFriendsChecker import getSuggestion
from lxml import etree
import os, operator
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

def printTopWords(words, n):
    words_sorted = sorted(words.iteritems(), key=operator.itemgetter(1), reverse=True)
    for i in range(0, n):
        pair = words_sorted[i]
        print(str(pair[1]) + " " + pair[0])

def analyze(dir_input):
    print(str(datetime.datetime.now().time()) +  " start analyze " + dir_input )

    w_count = 0
    ff_count = 0
    ff_map = dict()
    files = os.listdir(dir_input)
    for file in files:
        xml_text = open(dir_input + file, "r")
        xml = etree.parse(xml_text)
        for element in xml.iter("event"):
            if element.text == None:
               continue
            sentence = cleanText(element.text)
            for word in sentence.split():
                w_count +=1
                if isFalseFriend(word):
                    print(word)
                    print(createSuggestion(getSuggestion(word)))
                    ff_count += 1
                    if word in ff_map:
                        ff_map[word] +=1
                    else:
                        ff_map[word] = 1
    print(ff_count, w_count)
    print(str(float(ff_count) / w_count * 100))
    #print(ff_map)
    printTopWords(ff_map, len(ff_map))



analyze('../gewiss/DEU_L2_UK_EV/')
#analyze('../gewiss/DEU_L2_UK_PG/')
#analyze('../gewiss/DEU_L2_UK_SV/')

#if isFalseFriend("vor"):
#    print(createSuggestion(getSuggestion("vor")))