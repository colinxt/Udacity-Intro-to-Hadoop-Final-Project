#!/usr/bin/python

import sys
import csv
import operator

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

reader.next()

#The dict of tags and counts for this running mapper
#Eg. d = { 'lesson4': 5, 'challenging': 99 }
d = {}

for line in reader:
    if len(line) != 19:
        continue

    #Get a list of tags from a node
    tags = filter(None, line[2].split(' '))

    #Save counts
    for t in tags:
        if t in d:
            d[t] += 1
        else:
            d[t] = 1

#Get mapper's top 10
#Format: [('python', 59), ('unit2': 33)]
top_ten = sorted(d.iteritems(), key=operator.itemgetter(1), reverse=True)[:10]

#print out
writer.writerow(top_ten)
