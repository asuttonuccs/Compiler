# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 11:27:47 2018

@author: Adric
"""
import re
class JackTokenizer():

    
    def __init__(self, filename):
        self.TOKEN_TYPES = ["KEYWORD", "SYMBOL", "INT_CONST", "STRING_CONST", "IDENTIFIER"]
        self.KEYWORDS = ["class", "constructor", "function", "method", "field", "static", "var", "int", "char", "boolean", "void",
                "true", "false", "null", "this", "let", "do", "if", "else", "while", "return"]
        self.SYMBOLS = ['{','}','(',')','[',']','.',',',';','+','-','*','/','&','|','<','>','=','~']
        self.WHITESPACE = [' ', '\n', '\t']
        self.INT_CONSTS = re.compile('(\d).*$')
        self.STRING_CONSTS = re.compile('\"([^\n]*)\"')
        self.IDENTIFIERS = re.compile('([A-Za-z_]\w*)')
        self.tokenList = []
        self.filename = filename
        self.tokenizedList = []
        #Trying to open file if it doesnt exist prints unable to open
        try:
            self.file = open(filename,'r')
        except IOError as e:
            print ("Unable to open file")
            
        self.currentToken = ""
        for line in self.file:
            line = line.strip()
            if not line.startswith('//') and len(line) !=0:
                self.tokenList.append(line)
    
    def hasMoreTokens(self):    
        if len(self.tokenList) ==0:
            return False
        else:
            return True
    
    
    def tokenType(self):
        if (self.currentToken) in self.KEYWORDS:
            tok = "KEYWORD"
        elif(self.currentToken) in self.SYMBOLS:
            tok = "SYMBOL"
        elif(self.IDENTIFIERS.match(self.currentToken)):
            tok = "IDENTIFIER"
        elif(self.INT_CONSTS.match(self.currentToken)):
            tok = "INT_CONST"
        elif(self.STRING_CONSTS.match(self.currentToken)):
            tok = "STRING_CONST"
        else:
            tok = "UNDEFINED"
        
        return tok
    
    
    
    
    
    #STILL WORKING ON THIS ADVANCE ISNT MOVING ON AND DOES TOO MUCH?
    def advance(self):
        if self.hasMoreTokens():
            tokenInProgress = []
            tok = ""
            targetChar=""
            currentLine = self.tokenList[0]
            print(currentLine)
            
            print(currentLine[0])
            
            #This takes the line and breaks it into tokens in current line then characters in token so that if it is a symbol or whitespace it wont be part of the same token
            for token in currentLine:
                for char in token:
                    print("CHAR IS:" + char + "TYPE IS: " + str(type(char)))
                    if ((char not in self.SYMBOLS) and (char not in self.WHITESPACE)):
                        print("INSIDE not symbol or whitespace with char: " + char)
                        tok = tok + char
                        print (targetChar)
                    #it is a symbol
                    elif(char in self.SYMBOLS):
                        tokenInProgress.append(char)
                        #checks to make sure its not empty
                        if tok:
                            tokenInProgress.append(tok)
                            tok = ""
                    #it is a whitespace
                    elif(char in self.WHITESPACE):
                        #checks to make sure its not empty
                        if tok:
                            tokenInProgress.append(tok)
                            tok = ""
                    else:
                        print("ERROR")
            #checks to make sure its not empty
            if tok:
                tokenInProgress.append(tok)

            for token in tokenInProgress:
                self.tokenizedList.append(token)
            self.tokenList.pop()
            print(tokenInProgress)
            #self.currentToken = self.tokenList[0] 
            #self.tokenList.pop(0)

        
jack = JackTokenizer("test.txt")
print(jack.tokenType())
jack.advance()
jack.advance()
jack.advance()
print(jack.tokenizedList)