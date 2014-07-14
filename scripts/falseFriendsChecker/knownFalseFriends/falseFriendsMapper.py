import csv
import os, codecs


ffmap = list()

def get(word):
    return word.lower()

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = codecs.open(os.path.join(location, "falseFriends.csv"), "r")
reader = csv.reader(f, delimiter=',')
for row in reader:
    ffmap.append((get(row[0]),get(row[1]),get(row[2]),get(row[3])))
f.close()



