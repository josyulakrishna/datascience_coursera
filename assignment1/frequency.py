'''
Created on May 6, 2013

@author: Josyula
'''
from __future__ import division
from string import *
import json
import sys
import re

#===============================================================================
# '''
# The frequency of a term can be calculate with the following formula:
# [# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets]
#===============================================================================

def term_frequency(tweet_file): 
    term_fre = dict()
#    unwanted_chars = dict.fromkeys(map(ord, ':;,.!?'), None)
    for line in tweet_file: 
        result = json.loads(line)
        if 'text' in result.keys():
            tweet = result['text'].split()            
            #print tweet
            for word in tweet:
                term_fre[word] = term_fre.get(word,1) + 1
                
    return term_fre

def total_count(term_fre): 

    totalfre = 0
    for k,v in term_fre.iteritems(): 
        totalfre = totalfre + v
    return totalfre

def print_results(totalfre, term_fre):
#     outputfile = open('E:\\temp.out','w')
     for k ,v in term_fre.iteritems():
         value = v/totalfre
         sys.stdout.write('{0}\t{1}\n' .format(k.encode('utf-8') ,value))         
#     outputfile.close()
    

def main():
        
    tweet_file = open(sys.argv[1])#'('E:\\Data Science\\Assignments\\datasci_course_materials\\assignment1\\output.txt')#
    term_fre = term_frequency(tweet_file)
    totalfre = total_count(term_fre)
    print_results(totalfre, term_fre)
    
    

if __name__ == '__main__':
    main()    