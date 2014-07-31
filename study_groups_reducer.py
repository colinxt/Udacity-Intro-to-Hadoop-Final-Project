#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

#The master dict of nodes
d = {}

for line in reader:
    #Save the node
    if line[2] == 'question':
        if line[0] in d:
            d[line[0]].append(line[1])
        else:
            d[line[0]] = [line[1]]
    else:
        #Get the post id of this node
        pid = line[3]
        if pid in d:
            #If exists, add itself
            d[pid].append(line[1])
        else:
            #If not, create one
            d[pid] = [line[1]]

#print out
for i in d:
    writer.writerow([i, d[i]])
