# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 12:57:27 2018

@author: Adric
"""
from Parser import Parser
def main():
    parser = Parser("README.MD")
    parser.advance()
    while parser.hasMoreCommands():
        print(parser.commandType())
        parser.advance()
    print(parser.commandType())
    parser.close()
main()