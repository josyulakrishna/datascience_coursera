'''
Created on May 6, 2013

@author: Josyula
'''
import json
import sys
import operator 
from collections import defaultdict

def extract_hashtag(tweet_file):
    hashtag_count = defaultdict(float)
    hashtags = []
    tweet_file.seek(0)
    for line in tweet_file:
        result = json.loads(line)
        if  result.has_key('entities'): 
            if len(result['entities']['hashtags']) > 0:
                for tags in result['entities']['hashtags']:
                    tag = tags.get('text')
                    hashtags.append(tag) 
        else:
            continue 
    
    for hashtag in hashtags:
        hashtag_count[hashtag] = hashtag_count[hashtag] + 1 
    
#    for hashtag in hashtags :                
#        hashtag_count[hashtag] = hashtag_count.get(hashtag, 1) + 1
#        
    print_results(hashtag_count)

def print_results(hashtag_map):
    sorted_map = sorted(hashtag_map.iteritems(), key=operator.itemgetter(1),reverse = True)
#    sys.stdout.write("{0}\t{1}\n" .format(sorted_map[11][0],float(7)))
    for i in range(10):
        outputString = "{0}\t{1}" .format(sorted_map[i][0],sorted_map[i][1])
        print outputString.encode('utf-8')
    
    

def main():    
    tweet_file = open(sys.argv[1])#'E:\\Data Science\\Assignments\\datasci_course_materials\\assignment1\\output.txt') #output.txt
    extract_hashtag(tweet_file)
    

if __name__ == '__main__':
    main()
