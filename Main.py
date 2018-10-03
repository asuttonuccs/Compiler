# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 12:57:27 2018

@author: Adric
"""
from Parser import Parser
from CodeWriter import CodeWriter
def main():
    parser = Parser("README.MD")
    codewriter = CodeWriter("Test", parser)
    parser.advance()
    while parser.hasMoreCommands():
        parser.advance()
        if parser.currentCommand.split(' ')[0] == 'push' or parser.currentCommand.split(' ')[0] == 'pop':
            codewriter.WritePushPop(parser.currentCommand.split(' ')[0], parser.arg2(), parser.currentCommand.split(' ')[2])
        if parser.commandType() == 'C_ARITHMETIC':
            codewriter.writeArithmetic(parser.currentCommand)
            
        
    #codewriter.testwrite(parser.currentCommand)
    parser.close()
main()