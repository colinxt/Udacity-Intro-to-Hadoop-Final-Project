#!/usr/bin/python

import sys
import csv


reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

reader.next()

for line in reader:
    if len(line) != 19:
        continue

    #only get the hour (such as '08', '21', or '00')
    time = line[8][11:13]

    writer.writerow([line[3], time])
