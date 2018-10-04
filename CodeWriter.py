# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 10:00:16 2018

@author: Adric
"""

class CodeWriter():
    def __init__(self,outputfile):
        self.outputfile = outputfile
        self.counter = 0
        try:
            self.file = open(outputfile,'w')
        except IOError as e:
            print ("Unable to open file")
        self.name = ''
                
            
            
    def setFileName(self,name):
        self.name = name
        print("Working on file: " + name)
    def writeArithmetic(self, command):
        if (command.strip() in ["eq","gt","lt"]):
            counter = str(self.count())
        else:
            counter = str(self.counter)
        commandsDict = {
                "add": "\n//ADD\n@SP\nAM=M-1\nD=M\nA=A-1\nM=D+M\n",
                "sub": "\n//SUB\n@SP\nAM=M-1\nD=M\nA=A-1\nM=M-D\n",
                "neg": "\n//NEG\n@SP\nA=M-1\nM=-M\n",
                "and": "\n//AND\n@SP\nAM=M-1\nD=M\nA=A-1\nM=D&M\n",
                "or": "\n//OR\n@SP\nAM=M-1\nD=M\nA=A-1\nM=D|M\n",
                "eq": "\n//EQ\n@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@EQ.true." + counter + "\nD;JEQ\n@SP\nA=M-1\nM=0\n@EQ.follow." + counter + "\n0;JMP\n(EQ.true." + counter + ")\n@SP\nA=M-1\nM=-1\n(EQ.follow." + counter + ")\n",
                "gt": "\n//GT\n@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@GT.true." + counter + "\n\nD;JGT\n@SP\nA=M-1\nM=0\n@GT.follow." + counter + "\n0;JMP\n(GT.true." + counter + ")\n@SP\nA=M-1\nM=-1\n(GT.follow." + counter + ")\n",
                "lt": "\n//LT\n@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@LT.true." + counter + "\nD;JLT\n@SP\nA=M-1\nM=0\n@LT.follow." + counter + "\n0;JMP\n(LT.true." + counter + ")\n@SP\nA=M-1\nM=-1\n(LT.follow." + counter + ")\n",
                "not": "\n//NOT\n@SP\nA=M-1\nM=!M\n"
                }
        self.file.write(commandsDict.get(command.strip()))
    def WritePushPop(self, command, segment, index):
        if command == "push":
            if segment == "constant":
                #this first one needs to be what is being pushed not @const
                self.file.write("\n//PUSH CONST\n@" + index + "\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            elif segment == "local":
                self.file.write("\n//PUSH LCL\n@LCL\nD=M\n@"+ index +"\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            elif segment == "argument":
                self.file.write("\n//PUSH ARG\n@ARG\nD=M\n@"+ index +"\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            elif segment == "this":
                self.file.write("\n//PUSH THIS\n@THIS\nD=M\n@"+ index +"\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            elif segment == "that":
                self.file.write("\n//PUSH THAT\n@THAT\nD=M\n@"+ index +"\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            elif segment == "pointer":
                if index == '0':
                    self.file.write("\n//POINTER\n@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
                else:
                    self.file.write("\n//POINTER\n@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
                    
            elif segment == "static":
                self.file.write("\n//PUSH STATIC\n@" + self.outputfile + "." +index + "\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            elif segment == "temp":
                self.file.write("\n//PUSH TEMP\n@R5\nD=A\n@" + index + "\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            else:
                self.file.write("ERROR ERROR ERROR ERROR ERROR: " + command + segment + index)
                
        if command == "pop":
            if segment == "local":
                self.file.write("\n//POP LCL\n@LCL\nD=M\n@" + index + "\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n")
            elif segment == "argument":
                self.file.write("\n//POP ARG\n@ARG\nD=M\n@" + index + "\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n")
            elif segment == "this":
                self.file.write("\n//POP THIS\n@THIS\nD=M\n@" + index + "\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n")
            elif segment == "that":
                self.file.write("\n//POP THAT\n@THAT\nD=M\n@" + index + "\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n")
            elif segment == "pointer":
                if index == '0':
                    self.file.write("\n//POP POINTER\n@THIS\nD=A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n")
                else:
                    self.file.write("\n//POP POINTER\n@THAT\nD=A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n")
            elif segment == "static":
                self.file.write("\n//POP STATIC\n@" + self.outputfile + "." + index + "\nD=A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n")
            elif segment == "temp":
                self.file.write("@R5\nD=A\n@" + index + "\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n")
            else:
                self.file.write("ERROR ERROR ERROR ERROR ERROR"  + command + segment + index)
    def count(self):
        currentCount = self.counter
        self.counter = self.counter + 1
        return currentCount
    def Close(self):
         self.file.close()
         
    def translate(self, command):
        pass
    def testwrite(self,args):
        self.file.write(args)


