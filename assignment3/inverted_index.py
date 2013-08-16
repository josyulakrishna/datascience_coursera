'''
Created on May 22, 2013

@author: Josyula
'''
# Part 1
import MapReduce
import sys
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    document_id = record[0]
    text = record[1]
    words = text.split()
    for w in words:
      mr.emit_intermediate(w, document_id)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    docs = set(list_of_values)
    doct = list(docs)
    mr.emit((key, doct))

# Part 4
dpath = 'E:\\Data Science\\assignment3\\data\\books.json'
inputdata = open(dpath)
mr.execute(inputdata, mapper, reducer)