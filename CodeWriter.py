# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 10:00:16 2018

@author: Adric
"""

class CodeWriter():
    def __init__(self,outputfile,parser):
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
                "add": "\n//ADD\n@SP\nAM=M-1\nD=M\nA=A-1\nM=D+M\n",
                "sub": "\n//SUB\n@SP\nAM=M-1\nD=M\nA=A-1\nM=M-D\n",
                "neg": "\n//NEG\n@SP\nA=M-1\nM=-M\n",
                "and": "\n//AND\n@SP\nAM=M-1\nD=M\nA=A-1\nM=D&M\n",
                "or": "\n//OR\n@SP\nAM=M-1\nD=M\nA=A-1\nM=D|M\n",
                "eq": "D;JEQ",
                "gt": "D;JGT",
                "lt": "D;JLT",
                "not": "\n//NOT\n@SP\nA=M-1\nM=!M\n"
                }
        self.file.write(commandsDict.get(command.strip()))
    def WritePushPop(self, command, segment, index):
        if command == "push":
            if segment == "constant":
                #this first one needs to be what is being pushed not @const
                self.file.write("\n//PUSH CONST\n")
                self.file.write('@' + index)
                self.file.write('D=A\n')
                self.file.write('@SP\n')
                self.file.write('A=M\n')
                self.file.write('M=D\n')
                self.file.write('@SP\n')
                self.file.write('M=M+1\n')
            if segment == "local":
                self.file.write("\n//PUSH LCL\n@LCL\nD=M\n@"+ index +"A=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            if segment == "argument":
                self.file.write("\n//PUSH ARG\n@ARG\nD=M\n@"+ index +"A=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            if segment == "this":
                self.file.write("\n//PUSH THIS\n@THIS\nD=M\n@"+ index +"A=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            if segment == "that":
                self.file.write("\n//PUSH THAT\n@THAT\nD=M\n@"+ index +"A=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            if segment == "pointer":
                if index == '0':
                    self.file.write("\n//POINTER\n@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
                else:
                    self.file.write("\n//POINTER\n@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
                    
                    #NEED TO FIX THIS ONE
            if segment == "static":
                self.file.write("//\nPUSH STATIC\n@" + self.outputFile + "." +index + "\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            if segment == "temp":
                self.file.write("@R5\nD=A\n@" + index + "\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
                
        if command == "pop":
            pass
            
        
    def Close(self):
         self.file.close()
         
    def translate(self, command):
        pass
    def testwrite(self,args):
        self.file.write(args)


