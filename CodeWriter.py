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
        self.LCL = 1015
        self.TEMP = 5
        self.REGISTERS = 13
        self.STATIC = 16
        self.STACK = 256
        
        
            
            
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
        if command == "push":
            if segment == "constant":
                #this first one needs to be what is being pushed not @const
                self.file.write('@ CONST+index')
                self.file.write('D=A')
                self.file.write('@SP')
                self.file.write('A=M')
                self.file.write('M=D')
                self.file.write('@SP')
                self.file.write('M=M+1')
        if command == "pop":
            
        
    def Close(self):
        self.file.close()
        
Test = CodeWriter("outTest")
Test.writeArithmetic("sub")
Test.Close()