import sys
import json
import re

def tweet_word_scores(tweet_file):
    fields = dict()
    for line in tweet_file: 
        field = line.split("\t")
        fields[field[0]] = field[1]
    return fields

def cal_sentiment(sent_file,sentiment_scores):        
    new_word_sentiment = {}
    pos,neg =1,1
    for line in sent_file: 
        result = json.loads(line)
        if 'text' in result.keys():            
            tweet = result['text'].split()    
            sentimentscore = 0.0
            #calculating Sentiment score of tweets with unknown words to 0
            for word in tweet:        
                if word.encode('utf-8') in sentiment_scores.keys():
                    sentimentscore = float(sentimentscore) + float(sentiment_scores[word])
    
                    if sentiment_scores[word] > 0:
                            pos += 1;
                    else: 
                            neg +=1 
            
            for word in tweet:            
                if word not in sentiment_scores.keys():            
                    new_word_sentiment[word] = sentimentscore*(float(pos)/float(neg)) + new_word_sentiment.get(word,1)
                    
    print_results(sent_file,new_word_sentiment,sentiment_scores)

def print_results(sent_file,new_words_sentiment,sentiment_scores):     
#    outputfile = open('E:\\myoutput.txt','w')
#    mylist = list()
#z  = dict(sentiment_scores.items() + new_words_sentiment.items())
    sent_file.seek(0)
    for line in sent_file: 
        result = json.loads(line)
        if 'text' in result.keys():
            tweet = result['text'].split()  
            #calculating Sentiment score of tweets with unknown words to 0
            for word in tweet:
                if word in new_words_sentiment.keys():
                     outputString = '{0}\t{1}'.format(word ,new_words_sentiment[word])
                     print outputString.decode('utf-8')                     
#                     outputfile
#    outputfile.close()
    
                    
    
def main():
    sent_file = open(sys.argv[1]) #af111.out
    tweet_file = open(sys.argv[2]) #output.txthw()
#    sent_file = open('E:\\Data Science\\Assignments\\datasci_course_materials\\assignment1\\AFINN-111.txt') #sys.argv[1] #af111.out
#    tweet_file = open('E:\\Data Science\\Assignments\\datasci_course_materials\\assignment1\\testoutput.txt') #sys.argv[2] #output.txt    
    sentiment_scores = tweet_word_scores(sent_file)
    cal_sentiment(tweet_file,sentiment_scores)
    sent_file.close()
    tweet_file.close()
    

if __name__ == '__main__':
    main()
