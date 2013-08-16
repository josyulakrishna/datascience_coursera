'''
Created on May 14, 2013

@author: Josyula
'''
#
import sqlite3 as sql
import sys
def main(): 
    dbpath =  'E:\\Data Science\\Assignments\\datasci_course_materials\\assignment2\\reuters.db'
    con = sql.connect(dbpath)

    with con:
        #td2 = txt_earn $td1 = txt_crude
        cur = con.cursor()                                    
        cur.execute("SELECT term FROM Frequency where docid='17035_txt_earn' Except SELECT term FROM Frequency where docid ='10080_txt_crude';")        
        rows = cur.fetchall()
        for item in rows:
           cur.execute("insert into newt values ('10080_txt_crude',?,0)", item)
            
        
if __name__ =='__main__' :
    main()
    