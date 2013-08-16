'''
Created on May 4, 2013

@author: Josyula
'''
import urllib
import json
outputfile = open('E:\\Data Science\\Assignments\\datasci_course_materials\\assignment1\\tenpages.txt','w' )
for i in range(1,11):
    response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page="+str(i))  #@UndefinedVariable
    presponse = json.load(response)
    for i in range(len(presponse['results'])):
        outputfile.write(presponse['results'][i]['text'].encode('utf-8')+"\n")
outputfile.close()
