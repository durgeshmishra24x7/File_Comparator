# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:34:53 2020

@author: Durgesh_Mishra
"""

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Language: Python 3.7.6
#Author : Durgesh Mishra

import os,sys
import difflib
import docx2txt as dx



import File_Comparator_GUI as FCG

class compar:
    
    global path,path2,result,result2,test1,test2,diff
    
   
    
    #path=input("Provide the path of first file :- ")
    #path2=input("Provide the path of second file:- ")
    
    def __init__(self,path,path2):
        self.path = path
        self.path2 =path2
        print(self.path)
    #path="C:/Users/SHBG7410/Desktop/Alter/doc/test1.docx"
    #path2="C:/Users/SHBG7410/Desktop/Alter/doc/test2.docx"
class rend(compar):
    global word,word1,word2,word3
    def proc(self,path,path2):
        self.result = dx.process(path)
        self.result2 = dx.process(path2)
        
    def testing(self):
        self.test1 = open("test1","w+",encoding='utf8')
        self.test1.write(self.result)
        self.test2 = open("test2","w+",encoding='utf8')
        self.test2.write(self.result2)
        
        self.test1.close()
        self.test2.close()
        
    def reading(self):
        self.ff = open("test1","r+",encoding='utf8')
        self.sf = open("test2","r+",encoding='utf8')
        self.r1=self.ff.read()
        self.r2=self.sf.read()
        self.word2,self.word3=[],[]
        for self.word in self.result.split():
            self.word2.append(self.word)
        for self.word1 in self.result2.split():
            self.word3.append(self.word1)
        
    def HTML(self):
        self.diff=difflib.HtmlDiff().make_file(self.word2,self.word3)
        self.dr=open("difference_report.html",'w',encoding='utf8')
        self.dr.write(self.diff)
        self.dr.close()
        
    def OUTPUT(self):
        
        self.url="difference_report.html"
        os.startfile(self.url)
'''
if __name__=="__main__":
    FCG.app.resp()
    FCG.gui.compare()
    COMP=compar()
    
    REND=rend()
    REND.proc(path,path2)
    REND.testing()
    
    REND.reading()
    REND.HTML()
    REND.OUTPUT()
    
'''   


# In[ ]:




