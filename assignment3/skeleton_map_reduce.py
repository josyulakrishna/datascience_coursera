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
    pass
#Part 3
def reducer(key, list_of_values):
    pass
    
# Part 4
#dpath = 'E:\\Data Science\\assignment3\\data\\books.json'
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)