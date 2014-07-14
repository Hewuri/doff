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

sentence = "dies ist ein test jetzt werde ich konkret und sage meine kritik"
for word in sentence.split():
    if isFalseFriend(word):
        print(word + " " +  createSuggestion(getSuggestion(word)))


'''w = list()
def analyze(dir_input, name):
    print(str(datetime.datetime.now().time()) +  " start analyze " + name )
    nodeSoap = etree.Element(name.replace(" ","_"))
    files = ['testdata.xml'] if name == "Testdata" else os.listdir(dir_input)
    files.sort()

    for file in files:
        xml_text = codecs.open(dir_input + file, "r", "utf-8")
        xml = etree.parse(xml_text)
        text = ""
        for element in xml.iter("p"):
            if element.text != None:
                text += " "  + cleanText(element.text)
        init_postagger(text)
        nodeEpisode = etree.Element("episode_" +file.replace(".xml", ""))
        nodeEpisode.attrib["year"] = xml.getroot().attrib["year"]
        for element in xml.iter("p"):
            if element.text == None or element.text.strip() == "Dahoam is Dahoam.":
                continue
            sentence = cleanText(element.text)
            nodeText = ""
            for word in sentence.split():
                if isAnglicism(word, sentence):
                    nodeText += "<a>" + word +"</a> "
                    w.append(word)
                    print(word + " -> " + sentence + " -> " + file)
                else:
                    nodeText += word + " "
            if "</a>" in nodeText:
                nodeElement = element
                nodeElement.text = nodeText
                nodeEpisode.append(nodeElement)
        nodeSoap.append(nodeEpisode)
    print(str(datetime.datetime.now().time()) +  " finish analyze " + name)
    return nodeSoap


resultXml = etree.Element('root')
#resultXml.append(analyze('../scripts/', 'Testdata'))
resultXml.append(analyze('../subtitles/Lindenstrasse/normalized/', 'Lindenstrasse'))
resultXml.append(analyze('../subtitles/Dahoam is Dahoam/normalized/', 'Dahoam is Dahoam'))

file = open("results/result.xml","w")
file.write(etree.tostring(resultXml, pretty_print=True))
file.close()

'''