# -*- coding: utf-8 -*-
"""
Parser for Compiler Design
Created on Sun Sep 23 12:30:46 2018

@author: Adric
"""

class Parser():
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, "r")
        self.currentCommand = None
        
    def hasMoreCommands(self):
        moreCommands = True
        return moreCommands
    def advance(self):
        if self.hasMoreCommands():
            self.file.readline()
            
            
        
    
        