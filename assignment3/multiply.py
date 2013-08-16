'''
Created on May 22, 2013

@author: Josyula
'''
from collections import defaultdict
import MapReduce
import sys


#Part 1
mr = MapReduce.MapReduce()
mr_final = MapReduce.MapReduce()

data = open('matrix_final.json','w')

p_dict = defaultdict(list)
#Part2

def mapper(record):
    matrix = record[0]
    row    = record[1]
    col    = record[2]
    value  = record[3]
    if matrix == 'a' :        
        mr.emit_intermediate(col,(matrix,row, value))        
    else: 
        mr.emit_intermediate(row, (matrix, col, value))
    
#Part 3
def reducer(key, list_of_values):
    global p_dict 
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
#            mr1.emit_intermediate(a_list[m][0],b_list[n][0],a_list[m][1]*b_list[n][1])
                        


def mapper_final(record):
#    print record
    key = (record[0],record[1])
    value = record[2]
    mr_final.emit_intermediate(key,value)

def reducer_final(k,listOfValues):
    mr_final.emit((k[0],k[1],sum(listOfValues)))

    
# Part 4
dpath = 'E:\\Data Science\\assignment3\\data\\matrix.json'
inputdata = open(dpath)#sys.argv[1])
mr.execute(inputdata, mapper, reducer)

for k ,v in p_dict.iteritems(): 
    for i in range(len(v)):
        data.write("["+str(k[0])+","+str(k[1])+","+str(v[i])+"]\n")
    

data.close()

final_data = open('matrix_final.json')
mr_final.execute(final_data, mapper_final, reducer_final)