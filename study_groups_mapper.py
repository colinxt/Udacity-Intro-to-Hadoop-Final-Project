#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

reader.next()

for line in reader:
    if len(line) != 19:
        continue

    #Get node_id, author_id, node_type, abs_parent_id
    data = [line[0], line[3], line[5], line[7]]

    writer.writerow(data)
