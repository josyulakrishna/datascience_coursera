'''
Created on May 26, 2013

@author: Josyula
'''
from collections import defaultdict
import MapReduce
import sys


#Part 1
mr = MapReduce.MapReduce()
p_dict = defaultdict(list)
m_dict = defaultdict(list)

#Part2

def mapper(record):
    global m_dict
    matrix = record[0]
    row    = record[1]
    col    = record[2]
    value  = record[3]
    if matrix == 'a' :        
#        m_dict[col].append((matrix,row, value))                
        mr.emit_intermediate(col, (matrix,row, value))
    else: 
#        m_dict[row].append((matrix, col, value))
        mr.emit_intermediate(row, (matrix,col, value))
        
#Part 3

def reducer(key, list_of_values):
    a_list = []
    b_list = []
    for i in range(len(list_of_values)): 
        if list_of_values[i][0] == 'a':
            a_list.append((list_of_values[i][1],list_of_values[i][2])) 
        else : 
            b_list.append((list_of_values[i][1],list_of_values[i][2]))
    for m in range(len(a_list)) :
        for n in range(len(b_list)): 
            p_dict[(a_list[m][0],b_list[n][0])].append(a_list[m][1]*b_list[n][1])

    
# Part 4
#dpath = 'E:\\Data Science\\assignment3\\data\\matrix.json'
inputdata = open(sys.argv[1])#dpath)#
mr.execute(inputdata, mapper, reducer)
i_list =sorted(p_dict.keys(), key =lambda tup: tup) 

def answer(p_dict,i_list):
    for k, v in i_list: 
#    mr.emit( (k[0],k[1],sum(v)) )
        print [k,v,sum(p_dict[(k,v)])]  


answer(p_dict,i_list)