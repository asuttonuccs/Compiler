# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 10:00:16 2018

@author: Adric
"""

class CodeWriter():
    
    def __init__(self,outputfile):
        self.outputfile = outputfile
        self.name = outputfile.split('\\')[-1].replace('.asm','')
        self.counter = 0
        self.counterCall = 0
        try:
            self.file = open(outputfile,'w+')
        except IOError as e:
            print ("Unable to open file")
        #self.writeInit()
                
            
            
    def setFileName(self,name):
        self.name = name
        print("Working on file: " + name)
        
    
    def writeArithmetic(self, command):
        command = str(command.strip().split(" ")[0])
        if (command in ["eq","gt","lt"]):
            counter = self.count()
        else:
            counter = self.counter
            
        #These hold the commands that need to be written as asm code
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
        if commandsDict.get(command.strip()) == None:
            self.file.write("LOST COMMAND LOST COMMAND")
        else:
            self.file.write(commandsDict.get(command.strip()))
   
    #this takes care of all of the various push and pop commands
    def WritePushPop(self, command, segment, index):
        if command == "push":
            if segment == "constant":
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
                self.file.write("\n@R5\nD=A\n@" + index + "\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n")
            else:
                self.file.write("ERROR ERROR ERROR ERROR ERROR"  + command + segment + index)
    
    #This is the bootstrap code that takes care of stack and memory segment initialization
    def writeInit(self):
        self.file.write("\n//INITIALIZATION\n@256\nD=A\n@SP\nM=D\n")
        self.writeCall("Sys.init",0)
        self.file.write("0;JMP\n")
    #ASM unique labels
    def writeLabel(self,label):
        label = label.strip()
        self.file.write("\n//LABEL\n("+ self.name + "$"+label+")")
    def writeGoto(self,label):
        label = label.strip().strip(' ')
        self.file.write("\n//GOTO\n@"+ self.name + "$"+label+"\n0;JMP\n")
    def writeIf(self,label):
        label = label.strip()
        self.file.write("\n//IF\n@SP\nAM=M-1\nD=M\n@"+ self.name +"$"+label+"\nD;JNE\n")
    #Calls needed to have a counter to make them unique
    def writeCall(self,functionName,numArgs):
        functionName = functionName.strip()
        counter = self.counterCall
        self.couterCall = self.counterCall+1
        self.file.write("\n//CALL\n@SP\nD=M\n@R13\nM=D\n@RET."+str(counter)+"\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@LCL\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@ARG\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@R13\nD=M\n@"+str(numArgs)+"\nD=D-A\n@ARG\nM=D\n@SP\nD=M\n@LCL\nM=D\n@"+functionName+"\n0;JMP\n(RET."+ str(counter) +")\n")
    def writeReturn(self):
        self.file.write("\n//RETURN\n@LCL\nD=M\n@5\nA=D-A\nD=M\n@R13\nM=D\n@SP\nA=M-1\nD=M\n@ARG\nA=M\nM=D\nD=A+1\n@SP\nM=D\n@LCL\nAM=M-1\nD=M\n@THAT\nM=D\n@LCL\nAM=M-1\nD=M\n@THIS\nM=D\n@LCL\nAM=M-1\nD=M\n@ARG\nM=D\n@LCL\nAM=M-1\nD=M\n@LCL\nM=D\n@R13\nA=M\n0;JMP\n")
    #this may conflict with labels
    def writeFunction(self,functionName, numLocals):
        functionName = functionName.strip()
        numLocals = numLocals.strip()
        self.file.write("\n//FUNCTION\n("+functionName+")\n@SP\nA=M\n")
        for i in range (int(numLocals)):
            self.file.write("M=0\nA=A+1\n")
        self.file.write("D=A\n@SP\nM=D\n")
    
    #Keeps a counter running
    def count(self):
        currentCount = self.counter
        self.counter = self.counter +1
        return currentCount
    def Close(self):
         self.file.close()
    def fileWrite(self,text):
        self.file.write("//"+text)
         
    def translate(self, command):
        pass
    def testwrite(self,args):
        self.file.write(args)


