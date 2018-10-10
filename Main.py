# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 12:57:27 2018

@author: Adric
"""
import glob
import os
import sys
from Parser import Parser
from CodeWriter import CodeWriter
def main():
    #put the files in the same folder as the code and put the names in the filenames array, pass codewriter the name you want to output or filename[x] if you want it to be the same name with .asm
    #filenames = ["BasicTest","PointerTest","SimpleAdd","StackTest","StaticTest"]
   
    filesnames = []
    inputList = []
    ##put the file directory here
    filesPath = "C:\\Users\\drumm\\OneDrive\\Documents\\Code\\nand2tetris\\projects\\08\\FunctionCalls\\FibonacciElement\\"
    runInit = False
    
    inputList = glob.glob(filesPath +"*.vm")
    for x in range(0, len(inputList)):
        filesnames.append(inputList[x].split('\\')[-1].replace('.vm',''))
    print(filesnames)
    if len(inputList) > 1:
        runInit = True
    print("runINIT=" + str(runInit))

    
    

    
    
    for x in range(0,len(inputList)):
        
        
        filename = inputList[x]
        parser = Parser(filename)
        
        if runInit == True:
            print("READING: " + filesPath + inputList[0].split('\\')[-2].replace('.vm', '') +".asm")
            codewriter = CodeWriter(filesPath + inputList[0].split('\\')[-2].replace('.vm', '') +".asm")
            codewriter.writeInit()
        else:
            print(filesPath + filesnames[0] + ".asm")
            codewriter = CodeWriter(filesPath + filesnames[0] + ".asm")
        parser.advance()
        #I need to add the rest of the commands in next
        print(filesnames[x] + " hasmorecommands :" + str(parser.hasMoreCommands()))
        print("\nCurrentCom: " + str(parser.currentCommand))
        while parser.hasMoreCommands():
            parser.advance()
            print("\nCurrentCom: " + str(parser.currentCommand))
            if parser.currentCommand.split(' ')[0] == 'push' or parser.currentCommand.split(' ')[0] == 'pop':
                codewriter.WritePushPop(parser.currentCommand.strip().split(' ')[0], parser.arg2(), parser.currentCommand.strip().split(' ')[2])
            elif parser.commandType() == 'C_ARITHMETIC':
                codewriter.writeArithmetic(parser.currentCommand)
            elif parser.commandType() == 'C_LABEL':
                codewriter.writeLabel(parser.currentCommand.split(' ')[1])
            elif parser.commandType() == 'C_GOTO':
                codewriter.writeGoto(parser.currentCommand.split(' ')[1])
            elif parser.commandType() == 'C_IF':
                codewriter.writeIf(parser.currentCommand.split(' ')[1])
            elif parser.commandType() == 'C_CALL':
                codewriter.writeCall(parser.currentCommand.split(' ')[1],parser.currentCommand.split(' ')[2])
            elif parser.commandType() == 'C_RETURN':
                codewriter.writeReturn()
            elif parser.commandType() == 'C_FUNCTION':
                codewriter.writeFunction(parser.currentCommand.split(' ')[1],parser.currentCommand.split(' ')[2])
            else:
                #shouldnt hit this
                print("hitelse")
                print(parser.currentCommand +"\n")
                
        #codewriter.testwrite(parser.currentCommand)
        parser.close()
        print(filename)

    codewriter.Close()
main()