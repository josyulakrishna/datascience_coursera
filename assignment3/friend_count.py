'''
Created on May 22, 2013

@author: Josyula
'''

import MapReduce
import sys
#Part 1
mr = MapReduce.MapReduce()

#Part2 
def mapper(record):
    perB = record[0]
    mr.emit_intermediate(perB, 1)
#Part 3
def reducer(key, list_of_values):
    mr.emit((key, sum(list_of_values)))
    
# Part 4
#dpath = 'E:\\Data Science\\assignment3\\data\\friends.json'
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)