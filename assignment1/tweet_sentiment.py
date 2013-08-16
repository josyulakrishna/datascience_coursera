import sys
import json



def lines(fp):
    print str(len(fp.readlines()))

def tweet_word_scores(tweet_file):
    fields = dict()
    for line in tweet_file: 
        field = line.split("\t")
        fields[field[0]] = field[1]
    return fields

def cal_sentiment(sent_file,sentiment_scores):    
    
    myfile = open("E:\\sentiments.txt",'w')
    for line in sent_file: 
        result = json.loads(line)
        if 'text' in result.keys():
            tweet = result['text'].split(" ")    
            sentimentscore = 0.0
        
            for word in tweet:        
                if word in sentiment_scores.keys():
                    sentimentscore = float(sentimentscore) + float(sentiment_scores[word])
                         
            myfile.write("<sentiment:%f>\n" %sentimentscore)
    myfile.close()


def main():
    sent_file = open('E:\\Data Science\\Assignments\\datasci_course_materials\\assignment1\\AFINN-111.txt') #sys.argv[1] #af111.out
    tweet_file = open('E:\\Data Science\\Assignments\\datasci_course_materials\\assignment1\\output.txt') #sys.argv[2] #output.txt
    sentiment_scores = tweet_word_scores(sent_file)    
    cal_sentiment(tweet_file,sentiment_scores)
    sent_file.close()
    tweet_file.close()
    

if __name__ == '__main__':
    main()
