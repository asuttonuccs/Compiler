# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 12:57:27 2018

@author: Adric
"""
#
#CHECK IF TRUE comments probably a problem in vm
#
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
    filesPath = "C:\\Users\\drumm\\OneDrive\\Documents\\Code\\nand2tetris\\projects\\08\\FunctionCalls\\StaticsTest\\"
    runInit = False
    
    inputList = glob.glob(filesPath +"*.vm")
    for x in range(0, len(inputList)):
        filesnames.append(inputList[x].split('\\')[-1].replace('.vm',''))

    if len(inputList) > 1:
        runInit = True

    
    if runInit == True:
        codewriter = CodeWriter(filesPath + inputList[0].split('\\')[-2].replace('.vm', '') +".asm")
        codewriter.writeInit()
    else:
        codewriter = CodeWriter(filesPath + filesnames[0] + ".asm")
        
    
    for x in range(0,len(inputList)):
        
        filename = inputList[x]
        parser = Parser(filename)

        while parser.hasMoreCommands():
            parser.advance()
            if parser.arg1() == 'push' or parser.arg1() == 'pop':
                codewriter.WritePushPop(parser.arg1(), parser.arg2(), parser.arg3(),filename.split('\\')[-1].replace('.vm',''))
            elif parser.commandType() == 'C_ARITHMETIC':
                codewriter.writeArithmetic(parser.currentCommand)
            elif parser.commandType() == 'C_LABEL':
                codewriter.writeLabel(parser.arg2())
            elif parser.commandType() == 'C_GOTO':
                codewriter.writeGoto(parser.arg2())
            elif parser.commandType() == 'C_IF':
                codewriter.writeIf(parser.arg2())
            elif parser.commandType() == 'C_CALL':
                codewriter.writeCall(parser.arg2(),parser.arg3())
            elif parser.commandType() == 'C_RETURN':
                codewriter.writeReturn()
            elif parser.commandType() == 'C_FUNCTION':
                codewriter.writeFunction(parser.arg2(),parser.arg3())
            else:
                print("hitelse")

                

        parser.close()


    codewriter.Close()
main()