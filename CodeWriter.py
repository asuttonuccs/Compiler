# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 10:00:16 2018

@author: Adric
"""

class CodeWriter():
    def __init__(self,outputfile):
        self.outputfile = outputfile
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
                self.file.write("\n//PUSH CONST\n@" + index + "D=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            elif segment == "local":
                self.file.write("\n//PUSH LCL\n@LCL\nD=M\n@"+ index +"A=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            elif segment == "argument":
                self.file.write("\n//PUSH ARG\n@ARG\nD=M\n@"+ index +"A=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            elif segment == "this":
                self.file.write("\n//PUSH THIS\n@THIS\nD=M\n@"+ index +"A=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            elif segment == "that":
                self.file.write("\n//PUSH THAT\n@THAT\nD=M\n@"+ index +"A=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            elif segment == "pointer":
                if index == '0':
                    self.file.write("\n//POINTER\n@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
                else:
                    self.file.write("\n//POINTER\n@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
                    
                    #NEED TO FIX THIS ONE
            elif segment == "static":
                self.file.write("\n//PUSH STATIC\n@" + self.outputfile + "." +index + "D=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            elif segment == "temp":
                self.file.write("\n//PUSH TEMP\n@R5\nD=A\n@" + index + "A=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            else:
                self.file.write("ERROR ERROR ERROR ERROR ERROR: " + command + segment + index)
                
        if command == "pop":
            if segment == "local":
                self.file.write("\n//POP LCL\n@LCL\nD=M\n@" + index + "D=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n")
            elif segment == "argument":
                self.file.write("\n//POP ARG\n@ARG\nD=M\n@" + index + "D=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n")
            elif segment == "this":
                self.file.write("\n//POP THIS\n@THIS\nD=M\n@" + index + "D=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n")
            elif segment == "that":
                self.file.write("\n//POP THAT\n@THAT\nD=M\n@" + index + "D=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n")
            elif segment == "pointer":
                if index == '0':
                    self.file.write("\n//POP POINTER\n@THIS\nD=A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n")
                else:
                    self.file.write("\n//POP POINTER\n@THAT\nD=A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n")
            elif segment == "static":
                self.file.write("\n//POP STATIC\n@" + self.outputfile + "." + index + "D=A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n")
            elif segment == "temp":
                self.file.write("@R5\nD=A\n@" + index + "\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n")
            else:
                self.file.write("ERROR ERROR ERROR ERROR ERROR"  + command + segment + index)
        
    def Close(self):
         self.file.close()
         
    def translate(self, command):
        pass
    def testwrite(self,args):
        self.file.write(args)


