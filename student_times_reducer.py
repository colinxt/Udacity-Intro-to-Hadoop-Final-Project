#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

#a dictionary storing each author and a dictionary of her hours and counts
#Eg. {
#     '179839': {'19':2,'21':1},
#     '927178': {'00':4}
#    }
authors = {}

for line in reader:
    #get author id and hour
    au, hr = line

    #save this count in authors
    if au in authors:
        #if the hour exists, add one
        if hr in authors[au]:
            authors[au][hr] += 1
        else:
            # otherwise, create and assign it with one
            authors[au][hr] = 1
    else:
        #if the author not exists, create one and add the hour
        authors[au] = {hr: 1}

#find and print out the max of each student
for author in authors:
    #define the current max count and the result list
    #there might be a tie
    maxi = 0
    res = []

    #find and save results
    for hr, ct in authors[author].items():
        #if larger than the maximum
        if ct > maxi:
            #change the max to this hr
            maxi = ct
            #clear the res list and start with the current hr
            res = [hr]
        #if the au equals to the max count
        elif ct == maxi:
            #append current hr to the result
            res.append(hr)

    #print out
    for r in res:
        writer.writerow([author, r])
