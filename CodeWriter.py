# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 10:00:16 2018

@author: Adric
"""

class CodeWriter():
    #AM=M+-1 allows D=M to then have what the stack is and decrements the stack
    def __init__(self,outputfile):
        self.outputfile = outputfile
        self.counter = 0
        self.counterCall = 0
        try:
            self.file = open(outputfile,'w')
        except IOError as e:
            print ("Unable to open file")
        self.name = ''
                
            
            
    def setFileName(self,name):
        self.name = name
        print("Working on file: " + name)
    def writeArithmetic(self, command):
        command = command.strip()
        if (command in ["eq","gt","lt"]):
            counter = self.count()
        else:
            counter = self.counter
        commandsDict = {
                "add": "\n//ADD\n@SP\nAM=M-1\nD=M\nA=A-1\nM=D+M\n",
                "sub": "\n//SUB\n@SP\nAM=M-1\nD=M\nA=A-1\nM=M-D\n",
                "neg": "\n//NEG\n@SP\nA=M-1\nM=-M\n",
                "and": "\n//AND\n@SP\nAM=M-1\nD=M\nA=A-1\nM=D&M\n",
                "or": "\n//OR\n@SP\nAM=M-1\nD=M\nA=A-1\nM=D|M\n",
                "eq": "\n//EQ\n@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@EQ.true." + str(counter) + "\nD;JEQ\n@SP\nA=M-1\nM=0\n@EQ.follow." + str(counter) + "\n0;JMP\n(EQ.true." + str(counter) + ")\n@SP\nA=M-1\nM=-1\n(EQ.follow." + str(counter) + ")\n",
                "gt": "\n//GT\n@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@GT.true." + str(counter) + "\n\nD;JGT\n@SP\nA=M-1\nM=0\n@GT.follow." + str(counter) + "\n0;JMP\n(GT.true." + str(counter) + ")\n@SP\nA=M-1\nM=-1\n(GT.follow." + str(counter) + ")\n",
                "lt": "\n//LT\n@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@LT.true." + str(counter) + "\nD;JLT\n@SP\nA=M-1\nM=0\n@LT.follow." + str(counter) + "\n0;JMP\n(LT.true." + str(counter) + ")\n@SP\nA=M-1\nM=-1\n(LT.follow." + str(counter) + ")\n",
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
    
    def writeInit(self):
        self.file.write("//INITIALIZATION\n@256\nD=A\n@SP\nM=D\n" + self.writeCall("Sys.init",0) +"\n0;JMP\n")
    def writeLabel(self,label):
        self.file.write("//LABEL\n("+ self.name.replace('.vm','') + "$"+label+")")
    def writeGoto(self,label):
        self.file.write("//GOTO\n@"+ self.name.replace('.vm','') + "$"+label+"\n0;JMP\n")
    def writeIf(self,label):
        self.file.write("//IF\n@SP\nAM=M-1\nD=M\n@"+self.name.replace('.vm','')+"$"+label+"\nD;JNE\n")
    def writeCall(self,functionName,numArgs):
        counter = self.counterCall
        self.couterCall = self.counterCall+1
        self.file.write("//CALL\n@SP\nD=M\n@R13\nM=D\n@RET."+counter+"\nD+A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@LCL\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@ARG\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@R13\nD=m\n@"+numArgs+"\nD=D-A\n@ARG\nM=D\n@SP\nD=M\n@LCL\nM=D\n@"+functionName+"\n0:JMP\n(RET."+ counter +")\n")
    def writeReturn(self):
        self.file.write("//RETURN\n@LCL\nD=M\n@5\nA=D-A\nD=M\n@R13\nm=D\n@SP\nA=M-1\nD=M\n@ARG\nA=M\nM=D\nD=A+1\n@SP\nM=D\n@LCL\nAM=M-1\nD=M\n@THAT\nM=D\n@LCL\nAM=M-1\nD=M\n@THIS\nM=D\n@LCL\nAM=M-1\nD=M\n@ARG\nM=D\n@LCL\nAM=M-1\nD=M\n@LCL\nM=D\n@R13\nA=m\n0;JMP\n")
    #this may conflict with labels
    def writeFunction(self,functionName,numLocals):
        self.file.write("//FUNCTION\n("+functionName+")\n@SP\nA=M\n")
        for i in range (numLocals):
            self.file.write("M=0\nA=A+1\n")
        self.file.write("D=A\n@SP\nM=D\n")
    
    def count(self):
        currentCount = self.counter
        self.counter = self.counter +1
        return currentCount
    def Close(self):
         self.file.close()
         
    def translate(self, command):
        pass
    def testwrite(self,args):
        self.file.write(args)


