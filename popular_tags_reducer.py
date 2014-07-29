#!/usr/bin/python

import sys
import csv
import operator

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

#The master dict of tags and counts
d = {}

#separate and save all posts and answers
for line in reader:
    #Save tags and counts
    for tag in line:
        #Use eval() to convert string tuple to tuple for convenience
        t = eval(tag)
        
        #Save it
        if t[0] in d:
            t[0] += t[1]
        else:
            d[t[0]] = t[1]
            
#Get overall top ten
top_ten = sorted(d.iteritems(),key=operator.itemgetter(1),reverse=True)[:10]

#print out
for i in top_ten:
    writer.writerow(list(i))

