from falseFriendsChecker.falseFriendsChecker import isFalseFriend
from falseFriendsChecker.knownFalseFriends.knownFalseFriendsChecker import getSuggestion
from lxml import etree
import os, operator
from string import punctuation
from Tkinter import *
import Tkinter
import tkMessageBox

def cleanText(text):
    for c in punctuation:
        text = text.replace(c, " ")
    text = text.lower()
    text = text.replace("  ", " ")
    return text


def createSuggestion(l):
    if l:
        return l[0] + " [" + l[0] + "=" + l[1] + ", " + l[2] + "=" + l[3] + "]"
    return l[0] + " [no suggestion available]"



def displayText():

    global entryWidget
    result =""
    for word in cleanText(entryWidget.get()).split():
        if isFalseFriend(word):
            result += createSuggestion(getSuggestion(word)) + "\n"
    tkMessageBox.showinfo("", result)


if __name__ == "__main__":
    root = Tk()

    root["padx"] = 40
    root["pady"] = 20

    # Create a text frame to hold the text Label and the Entry widget
    textFrame = Frame(root)

    # Create a Label in textFrame
    entryLabel = Label(textFrame)
    entryLabel.pack(side=LEFT)

    # Create an Entry Widget in textFrame
    entryWidget = Entry(textFrame)
    entryWidget["width"] = 40
    entryWidget.pack(side=LEFT)

    textFrame.pack()

    button = Button(root, text="check", command=displayText)
    button.pack()

    root.mainloop()