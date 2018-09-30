# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 10:00:16 2018

@author: Adric
"""

class CodeWriter():
    def __init__(self,outputfile):
        try:
            self.file = open(outputfile,'w')
        except IOError as e:
            print ("Unable to open file")
        self.name = ''
        
            
            
    def setFileName(self,name):
        self.name = name
        print("Working on file: " + name)
    def writeArithmetic(self, command):
        commandsDict = {
                "add": "M=M+D",
                "sub": "M=M-D",
                "neg": "M=-M",
                "and": "M=M&D",
                "or": "M=M|D",
                "eq": "D;JEQ",
                "gt": "D;JGT",
                "lt": "D;JLT",
                "not": "M=!M"
                }
        self.file.write(commandsDict.get(command))
    def WritePushPop(self, command, segment, index):
        
        
    def Close(self):
        self.file.close()
        
Test = CodeWriter("outTest")
Test.writeArithmetic("sub")
Test.Close()