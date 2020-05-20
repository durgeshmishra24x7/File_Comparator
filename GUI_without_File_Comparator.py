# -*- coding: utf-8 -*-
"""
Created on Thu May 21 01:28:07 2020

@author: Durgesh Mishra
"""

from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import os
import os,sys
import difflib
import docx2txt as dx


class gui:
    
    global root,Name_of_app
    root = tk.Tk() 
    root.geometry('175x80') 
    Name_of_app="Comparator"
    root.title(Name_of_app)
    root.configure(background = "grey");

    global prof,fc,lst,file,p1,p2,btn,btn2,btn3
    global path,path2,result,result2,test1,test2,diff
    global word,word1,word2,word3
    st=[]
    def open_file(self,st):
        #c1=tk.filedialog.askdirectory()
        self.file = askopenfile(mode ='r', filetypes =[('Word Files', '*.docx',),('All Files')])
        if self.file: 
            self.prof=self.file.name
            st.append(self.prof)
            print(st)

    def compare(self):
    
        if self.st==[]:
            print("Select files first ")
        else:
            p1=self.st[0]
            p2=self.st[1]
            print("Path:- ",p1,"path2:- ",p2)
        
            self.result = dx.process(p1)
            self.result2 = dx.process(p2)
        
            self.test1 = open("test1","w+",encoding='utf8')
            self.test1.write(self.result)
            self.test2 = open("test2","w+",encoding='utf8')
            self.test2.write(self.result2)
        
            self.test1.close()
            self.test2.close()
        
            self.ff = open("test1","r+",encoding='utf8')
            self.sf = open("test2","r+",encoding='utf8')
            self.r1=self.ff.read()
            self.r2=self.sf.read()
            self.word2,self.word3=[],[]
            for self.word in self.result.split():
                self.word2.append(self.word)
                for self.word1 in self.result2.split():
                    self.word3.append(self.word1)
        
            self.diff=difflib.HtmlDiff().make_file(self.word2,self.word3)
            self.dr=open("difference_report.html",'w',encoding='utf8')
            self.dr.write(self.diff)
            self.dr.close()
        
            self.url="difference_report.html"
            os.startfile(self.url)
        
    
class app(gui):    
    def resp(self):        
        self.btn = tk.Button(root, text ='browse file 1',fg='white',bg='black',width=25, command = lambda:guiobj.open_file(self.st)) 
        self.btn.pack() 

        self.btn2=tk.Button(root, text ='browse file 2',fg='white',bg='black',width=25, command = lambda:guiobj.open_file(self.st)) 
        self.btn2.pack()

        self.btn3=tk.Button(root, text ='Compare',fg='Yellow',bg='black',width=25, command = lambda:guiobj.compare()) 
        self.btn3.pack()

if __name__=="__main__":
    
    APP=app()
    APP.resp()
    guiobj=gui()


mainloop()
