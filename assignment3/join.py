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
    order_id = record[1]
    t_row = record
    mr.emit_intermediate(order_id, t_row)

#Part 3
def reducer(key, list_of_values):
    
    opairs = []
    lpairs = [] 
    for i in range(len(list_of_values)):
        if list_of_values[i][0] == 'order' : 
            opairs.append(list_of_values[i])
        else :
            lpairs.append(list_of_values[i])
    
    for j in range(len(opairs)): 
        for i in range(len(lpairs)):  
          mr.emit(opairs[j]+lpairs[i])
            
            
            
            
         
        
# Part 4
#path = 'E:\\Data Science\\assignment3\\data\\records.json'
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)