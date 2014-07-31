#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

#a dictionary storing posts, its length, and a list of its answer lengths
#Eg. {
#     '179839': [120, [35,78]],
#     '927178': [223, [320]]
#    }
posts = {}

#separate and save all posts and answers
for line in reader:
    if line[1] == 'question':
        if line[0] not in posts:
            #if a question is not in posts, create a new one
            posts[line[0]] = [line[2], []]
    else:
        #if it's an answer
        if line[3] in posts:
            #find its parent(the questions), add the answer's length to the list
            posts[line[3]][1].append(line[2])
        else:
            #if the question not exists, create a new one
            posts[line[3]] = [0, [line[2]]]

for p in posts:
    #skip weird results
    if posts[p][0] == 0:
        continue
    #calculate the average length of answers of a post
    #if no answers, set the avg to zero
    if not posts[p][1]:
        ans_avg = 0
    else:
        #no need to convert to float
        ans_avg = sum(map(int, posts[p][1]))/len(posts[p][1])

    #print the result
    writer.writerow([p, posts[p][0], ans_avg])
