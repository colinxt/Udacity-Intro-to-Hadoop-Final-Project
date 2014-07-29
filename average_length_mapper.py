#!/usr/bin/python

import sys
import csv
 

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

reader.next()

for line in reader:
    if len(line) != 19:
        continue
    
    #for QUESTIONs and ANSWERs
    #get id, node_type, len of body, parent_ID 
    if line[5] != 'comment':
        newline = [line[0], line[5], len(line[4]), line[6]]
    
    writer.writerow(newline)

    
    

