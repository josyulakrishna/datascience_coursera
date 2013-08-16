'''
Created on May 9, 2013

@author: Josyula
'''
import json
import sys 
from collections import defaultdict
import operator

def tweet_word_scores(tweet_file):
    fields = dict()
    for line in tweet_file: 
        field = line.split("\t")
        fields[field[0]] = field[1]
    return fields


def parse_tweet_for_US(tweet_file,sentiment_scores):
    state_scores = defaultdict(float)
    for line in tweet_file: 
        result = json.loads(line)
        if result.has_key('text'):
                    if result.has_key('place'): 
                        if result['place']:
                            if result['place']['country_code'] =='US':                                 
                                sentimentscore = 0.0
                                #calculating Sentiment score of tweets with unknown words to 0
                                tweet = result['text'].split()
                                for word in tweet:        
                                    if word in sentiment_scores.keys():
                                        sentimentscore = float(sentimentscore) + float(sentiment_scores[word])
                                        
                                state_code = result['place']['full_name'].split()[-1]
                                state_scores[state_code] = state_scores[state_code] + sentimentscore
 
    print_results(state_scores)
    
def print_results(hashtag_map):
    sorted_map = sorted(hashtag_map.iteritems(), key=operator.itemgetter(1),reverse = True)
#    sys.stdout.write("{0}\t{1}\n" .format(sorted_map[11][0],float(7)))
    outputString = "{0}" .format(sorted_map[0][0])
    print outputString.encode('utf-8')


def main():
    sent_file = open(sys.argv[1]) #af111.out
    tweet_file = open(sys.argv[2]) #output.txthw()
#    sent_file = open('E:\\Data Science\\Assignments\\datasci_course_materials\\assignment1\\AFINN-111.txt') #sys.argv[1] #af111.out
#    tweet_file = open('E:\\Data Science\\Assignments\\datasci_course_materials\\assignment1\\output.txt') #sys.argv[2] #output.txt    
    sentiment_scores = tweet_word_scores(sent_file)
    parse_tweet_for_US(tweet_file,sentiment_scores)

if __name__ == '__main__': 
    main()
                
                 
                
        