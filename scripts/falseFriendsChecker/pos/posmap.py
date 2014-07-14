import csv
import os, codecs


posmap = dict()

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = codecs.open(os.path.join(location, "posmap.csv"), "r", "utf-8")
reader = csv.reader(f, delimiter=';')
for row in reader:
    posmap[row[0]]=row[1]
f.close()

