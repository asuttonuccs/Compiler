# -*- coding: utf-8 -*-
"""
Parser for Compiler Design
Created on Sun Sep 23 12:30:46 2018

@author: Adric
"""

class Parser():
    def __init__(self, filename):
        self.commandList = []
        self.filename = filename
        #Trying to open file if it doesnt exist prints unable to open
        try:
            self.file = open(filename,'r')
        except IOError as e:
            print ("Unable to open file")
            
        self.currentCommand = None
        for line in self.file:
            line = line.strip()
            if not line.startswith('//') and len(line) !=0:
                self.commandList.append(line)
        
        #These are the command types that should be looked for
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
                'if-goto':'C_IF',
                'function':'C_FUNCTION',
                'return':'C_RETURN',
                'call':'C_CALL',
                'label':'C_LABEL'
                }
    #Checks to see if there are more commands by calling peekLine
    def hasMoreCommands(self):
        
        if len(self.commandList) ==0:
            return False
        else:
            return True
        
    #Advances to the next command by making sure there are more
    def advance(self):
        if self.hasMoreCommands():
            self.currentCommand = self.commandList[0] 
            self.commandList.pop(0)


    def commandType(self):
        if self.commandDictionary.get(self.currentCommand.strip().split(' ')[0]):
            return self.commandDictionary.get(self.currentCommand.strip().split(' ')[0])
        
    def arg1(self):
       # if self.commandType() is not 'C_RETURN':
            return self.currentCommand.strip().split(' ')[0]
#        else:
#            print(self.currentCommand)
#            print("C_RETURN is not valid for arg1")
    def arg2(self):
        allowable = ['C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL','C_IF','C_GOTO','C_LABEL']
        if self.commandType() in allowable:
            return self.currentCommand.strip().split(' ')[1]
        else:
            print("{} are not valid for arg2".format(str(allowable)))
    def arg3(self):
        if len(self.currentCommand.split(' ')) > 2:
            return self.currentCommand.strip().split(' ')[2]
        else:
            print("ERROR ARG3 IS TOO SHORT")
    def close(self):
        self.file.close()
    
    
