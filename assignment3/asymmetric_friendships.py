'''
Created on May 22, 2013

@author: Josyula
'''

import MapReduce
import sys
from collections import Counter

#Part 1
mr = MapReduce.MapReduce()

#Part2 
def mapper(record):
    perA = record[0]
    perB = record[1]
    mr.emit_intermediate(perA, perB)
    mr.emit_intermediate(perB, perA)
#Part 3
def reducer(key, list_of_values):
    f_count = Counter(list_of_values)
    for k,v in f_count.iteritems(): 
        if v == 1 : 
            mr.emit((key,k))
    
    
# Part 4
#dpath = 'E:\\Data Science\\assignment3\\data\\friends.json'
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)