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
        self.MULTILINE_COMMENT = re.compile('/\*.*?\*/', flags=re.S)
        self.filename = filename
        self.tokenList = []
        
        #modifies the file by removing all comments
        self.removeComments()
        
        #Trying to open file if it doesnt exist prints unable to open
        try:
            self.file = open(filename + "modified",'r')
        except IOError as e:
            print ("Unable to open file")
        self.currentToken = ""
        
        
        # This reads in the tokens from the file

        self.readIn()


    
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
    
    def tokenCat(self):
        if self.currentToken in ['true','false','null','this']:
            tok = "KW_CONST"
        elif self.currentToken in ['int','char', 'boolean']:
            tok = "KW_TYPE"
        elif self.currentToken in ['static', 'field']:
            tok = "KW_VARDEC"
        elif self.currentToken in ['constructor', 'function', 'method']:
            tok = "KW_SUBDEC"
        elif self.currentToken == "var":
            tok = "KW_VAR"
        elif self.currentToken == "void":
            tok = "KW_VOID"
        elif self.currentToken == "class":
            tok = "KW_CLASS"
        elif self.currentToken == "let":
            tok = "KW_LET"
        elif self.currentToken == "if":
            tok = "KW_IF"
        elif self.currentToken == "else":
            tok = "KW_ELSE"
        elif self.currentToken == "while":
            tok = "KW_WHILE"
        elif self.currentToken == "do":
            tok = "KW_DO"
        elif self.currentToken == "return":
            tok = "KW_RETURN"
        elif self.currentToken == "(":
            tok = "SY_LPAREN"
        elif self.currentToken == ")":
            tok = "SY_RPAREN"
        elif self.currentToken == "[":
            tok = "SY_LBRACKET"
        elif self.currentToken  == "]":
            tok = "SY_RBRACKET"
        elif self.currentToken == "{":
            tok = "SY_LBRACE"
        elif self.currentToken == "}":
            tok = "SY_RBRACE"
        elif self.currentToken == ";":
            tok = "SY_SEMI"
        elif self.currentToken == ".":
            tok = "SY_PERIOD"
        elif self.currentToken == ",":
            tok = "SY_COMMA"
        elif self.currentToken == "=":
            tok = "SY_EQ"
        elif self.currentToken == "-":
            tok = "SY_MINUS"
        elif self.currentToken  == "~":
            tok = "SY_NOT"
        elif self.currentToken in ['+','*','/','&','|','<','>']:
            tok = "SY_OP"
        elif(self.IDENTIFIERS.match(self.currentToken)):
            tok = "IDENT"
        elif(self.INT_CONSTS.match(self.currentToken)):
            tok = "INTEGER"
        elif(self.STRING_CONSTS.match(self.currentToken)):
            tok = "STRING"
        else:
            tok = "BADTOKEN"
        return tok
    
    
    
    #STILL WORKING ON THIS ADVANCE ISNT MOVING ON AND DOES TOO MUCH?
    def advance(self):
        if self.hasMoreTokens():
            self.currentToken = self.tokenList[0]
            self.tokenList.pop(0)
            print("ADVANCED TOKEN IS NOW: " + self.currentToken)
            #self.currentToken = self.tokenList[0] 
            #self.tokenList.pop(0)
    def readIn(self):
        tok = ""
        stringFlag = False
        
        #for each line in file strip and remove empty lines or commented lines
        #Then for each char in line, if it is not a symbol or whitespace
        #build that token, when a symbol or white space is hit add the token to the list then reset token
        #if it is a string const ex. "Hello World" build it including whitespace and qoutes
        #Add the symbol as a token 
        #Once at end of line if there is a token that was being built append that token
        for line in self.file:
            
            line = line.strip()

            if not line.startswith('//') and len(line) !=0:

                for char in line:

                    if char == '"' and stringFlag == False:
                        tok = tok + char
                        stringFlag = True
                        continue
                    if(stringFlag == True):
                        #print(token)
                        if char == '"':
                            tok = tok + char
                            self.tokenList.append(tok)
                            print("the TOken is: "+ tok)
                            tok = ""
                            stringFlag = False
                            print("SET STRINGFLAG FALSE")
                            continue
                        else:
                            tok = tok + char
                            continue
                        

                    #print("CHAR IS:" + char + "TYPE IS: " + str(type(char)))
                    if ((char not in self.SYMBOLS) and (char not in self.WHITESPACE)):
                        #print("INSIDE not symbol or whitespace with char: " + char)
                        tok = tok + char
                    #it is a symbol
                    elif(char in self.SYMBOLS):
                        
                        #checks to make sure its not empty
                        if tok:
                            self.tokenList.append(tok)
                            tok = ""
                        self.tokenList.append(char)
                    #it is a whitespace
                    elif(char in self.WHITESPACE):
                        #checks to make sure its not empty
                        if tok:
                            self.tokenList.append(tok)
                            tok = ""
                    else:
                        print("ERROR")
                    print ("The token is :" + tok)
                #This is where when the line ends if there is a token being built it will add it to the list
                if tok:
                    self.tokenList.append(tok)
                    tok = ""
    #This makes a new file removing all of the comments from the file    
    def removeComments(self):
        try:
            self.file = open(self.filename ,'r')
        except IOError as e:
            print ("Unable to open file")
        file = open(self.filename, 'r')
        string = file.read()
        file.close()
        #removes multiline
        string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) # remove all  streamed comments (/*COMMENT */) from string
        #removes single line wherever it occurs and adds a new line
        string = re.sub(re.compile("//.*?\n" ) ,"\n" ,string) # remove all  singleline comments (//COMMENT\n ) from string
        try:
            modifiedFile = open(self.filename + 'modified', 'w')
        except IOError as e:
            print ("Unable to open file")
        
        modifiedFile.write(string)
        file.close()

        
        
jack = JackTokenizer("Main.jack")
print(jack.tokenList)
jack.advance()
jack.advance()