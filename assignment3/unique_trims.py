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
    gene = record[1]    
    mr.emit_intermediate("genes", gene[:-10]) 
    
#Part 3
def reducer(key, list_of_values):
    for value in set(list_of_values):
        mr.emit(value)
    
# Part 4
#dpath = 'E:\\Data Science\\assignment3\\data\\dna.json'
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)