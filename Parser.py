# -*- coding: utf-8 -*-
"""
Parser for Compiler Design
Created on Sun Sep 23 12:30:46 2018

@author: Adric
"""

class Parser():
    def __init__(self, filename):
        
        self.filename = filename
        #Trying to open file if it doesnt exist prints unable to open
        try:
            self.file = open(filename,'r')
        except IOError as e:
            print ("Unable to open file")
            
        self.currentCommand = None
        self.commandDictionary = {
                'add':'C_ARITHMETIC',
                'sub':'C_ARITHMETIC',
                'neg':'C_ARITHMETIC',
                'lt':'C_ARITHMETIC',
                'eq':'C_ARITHMETIC',
                'gt':'C_ARITHMETIC',
                'not':'C_ARITHMETIC',
                'and':'C_ARITHMETIC',
                'or':'C_ARITHMETIC',
                'push':'C_PUSH',
                'pop':'C_POP',
                'goto':'C_GOTO',
                'if':'C_IF',
                'function':'C_FUNCTION',
                'return':'C_RETURN',
                'call':'C_CALL',
                'label':'C_LABEL'
                }
    #Checks to see if there are more commands by calling peekLine
    def hasMoreCommands(self):
        nextLine = self.peekLine()
        if nextLine is None or nextLine == '':
            return False
        else:
            return True
    #Advances to the next command by making sure there are more
    def advance(self):
        if self.hasMoreCommands():
            self.currentCommand = self.file.readline()
    def commandType(self):
        if self.commandDictionary.get(self.currentCommand.strip().split(' ')[0]):
            return self.commandDictionary.get(self.currentCommand.strip().split(' ')[0])
        
    def arg1(self):
        if self.commandType() is not 'C_RETURN':
            return self.currentCommand.strip().split(' ')[0]
        else:
            print("C_RETURN is not valid for arg1")
    def arg2(self):
        allowable = ['C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL']
        if self.commandType() in allowable:
            return self.currentCommand.strip().split(' ')[1]
        else:
            print("{} are not valid for arg2".format(str(allowable)))
    def close(self):
        self.file.close()
    
    
    def peekLine(self):
        #to reposition spot in file
        pos = self.file.tell()
        line = self.file.readline()
        
        if line == "\n":
            line = self.file.readline()
            self.currentCommand = line
            pos = self.file.tell()
        #looking for comments
        while line.startswith('//'):
            
            pos = self.file.tell()
            line = self.file.readline().strip()
            if len(line.strip()) == 0:
                break
        
        #if at end of the file return the end of file
        if ("" == line):
            print("EOF")
            pos = self.file.tell()
            
        self.file.seek(pos)
        return line
        
#Testing
#Test = Parser("README.md")
#print(Test.currentCommand)
#print(Test.hasMoreCommands())
#Test.advance()
#print(Test.currentCommand)
#print("command is")
#print(Test.commandType())
#print("arg1 is")
#print(Test.arg1())
#print("arg2 is")
#print(Test.arg2())
#print(Test.hasMoreCommands())
#Test.advance()
#print(Test.currentCommand)
#print(Test.hasMoreCommands())
#
#Test.close()
        
            
            
            
        
    
        