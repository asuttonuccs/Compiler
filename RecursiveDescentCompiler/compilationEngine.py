# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:24:19 2018

@author: 999 Sutton
"""
import sys
from jackTokenizer import JackTokenizer
class CompilationEngine():
    #
    #This program parses tok files.
    #INPUT is a .tok file from the Jack language. title fileName as the file you want to input, must be in same folder or use path
    #OUTPUT is a .xml file with tags that break down the tokens into the syntax code
    #The program should show you what it expects if it is not there. For example if missing a closing } it will exit and tell you "expecting }"
    #
    
    #This tokenList has all the text in it. It is broken up into a tuple, each being recognized when it is the current token
    #It has(tokenType,token value)
    #the current token, always dealing with it before moving on to the next token
    

    def __init__(self, filename):
        self.operators = ['+', '-', '*', '/', '&','|','<','>','=']
        self.keyWords = ["class","constructor","function","method","field","static","var","int","char","boolean","void","true","false","null","this","let","do","if","else","while","return"]
        self.symbols = ['{','}','(',')','[',']','.',',',';','+','-','*','/','&','|','<','>','=','~']
        self.unops = ['-','~']
        self.keywordCost = ['true','false','null','this']
        self.outFile = open("{}.xml".format(filename.split(".")[0]), "w")
        self.jack = JackTokenizer(filename)
        print(self.jack.tokenList)
        if(self.jack.hasMoreTokens()):
            self.jack.advance()
            print(self.jack.currentToken)
            print(self.jack.tokenCat())
            if (self.jack.tokenCat() == "KW_CLASS"):
                self.compileClass()
        self.outFile.close()
    
    #def main():
    
        #Reads in the .tok file and puts it in a list in tuple form, with (Type,value)
    #    for line in inFile:
    #        tokenType = line.split(',',1)[0]
    #        tokenType.replace(' ', '')
    #        tokenValue = line.split(',',1)[1].strip('\n')
    #        tokenValue = tokenValue.lstrip(' ')
    #        tokenList.append([tokenType, tokenValue])
    
            
    #    if(999<len(tokenList) and self.jack.tokenCat() == "KW_CLASS"):
    #        selfcompileClass()
    #        
    #    inFile.close()
    #    self.outFile.close()
    
    #This takes care of the class construction the beginning of the grammar
    def compileClass(self):
        
        self.openTag("class")
        
        self.eatToken()
        self.jack.advance()
    
        if(self.jack.tokenCat() =="IDENT"):
            self.compileClassName()
        else:
            sys.exit("Invalid Syntax at number:{} token is:{}".format(999,self.jack.currentToken))
        if(self.jack.tokenCat() == "SY_LBRACE"):
            self.eatToken()
            self.jack.advance()
    
        else:
            sys.exit("Invalid Syntax at number:{} token is:{}".format(999,self.jack.currentToken))
        while(self.jack.tokenCat() == "KW_VARDEC"):
            self.compileClassVarDec()
        while(self.jack.tokenCat() == "KW_SUBDEC"):
            self.compileSubroutine()
        if(self.jack.tokenCat() == "SY_RBRACE"):
            self.eatToken()
            self.jack.advance()
        else:
            sys.exit("Invalid syntax expecting }} at number:{} token is:{}".format(999,self.jack.currentToken))
        self.closeTag("class")
        
    #This takes take of the class variable declarations        
    def compileClassVarDec(self):
    
        
        
        self.openTag("classVarDec")
        self.eatToken()
        self.jack.advance()
        
        #This takes the types into consideration along with className with the elif
        if(self.jack.tokenCat() == "KW_TYPE"):
            self.eatToken()
            self.jack.advance()
        elif(self.jack.tokenCat() == "IDENT"):
            self.compileClassName()
            
        while(self.jack.tokenCat() == "IDENT"):
            self.eatToken()
            self.jack.advance()
            if(self.jack.tokenCat() == "SY_COMMA"):
                self.eatToken()
                self.jack.advance()
        if(self.jack.tokenCat() == "SY_SEMI"):
            self.eatToken()
            self.jack.advance()
        else:
            sys.exit("Invalid Syntax missing ; at number:{} token is:{}".format(999,self.jack.currentToken))
        self.closeTag("classVarDec")
        
    #This takes care of the subroutine declarations
    def compileSubroutine(self):
    
        
        self.openTag("subroutineDec")
    
    #If it is a constructor it handles slightly differently
        if(self.jack.currentToken == "constructor"):
            self.eatToken()
            self.jack.advance()
            if(self.jack.tokenCat() == "IDENT"):
                self.compileClassName()
            else:
                sys.exit("Invalid syntax no class identifier for subroutine at number:{} token is:{}".format(999,self.jack.currentToken))
            if(self.jack.tokenCat() == "IDENT"):
                self.compileSubroutineName()
            else:
                sys.exit("Invalid syntax no indentifier for subroutine at number:{} token is:{}".format(999,self.jack.currentToken))
            if(self.jack.tokenCat() == "SY_LPAREN"):
                self.eatToken()
                self.jack.advance()
            else:
                sys.exit("Invalid syntax missing ( at number:{} token is:{}".format(999,self.jack.currentToken))
            if(self.jack.tokenCat() == "KW_TYPE"):
                self.compileParameterList()
                
            if(self.jack.tokenCat() == "SY_RPAREN"):
                self.eatToken()
                self.jack.advance()
            else:
                sys.exit("Invalid syntax missing ) at number:{} token is:{}".format(999,self.jack.currentToken))
            if(self.jack.tokenCat()== "SY_LBRACE"):
                self.compileSubroutineBody()
            else:
                sys.exit("Invalid syntax missing { at number:{} token is:{}".format(999,self.jack.currentToken))
        
    #If function or method it handles as follows    
        else:
            self.eatToken()
            self.jack.advance()
            if(self.jack.tokenCat() =="IDENT"):
                self.eatToken()
                self.jack.advance()
        
            elif(self.jack.tokenCat() == "KW_VOID" or self.jack.tokenCat() == "KW_TYPE"):
                self.eatToken()
                self.jack.advance()
            elif(self.jack.tokenCat() == "IDENT"):
                self.compileSubroutineName()
                
            else:    
                sys.exit("Invalid Syntax void or type missing at number:{} token is:{}".format(999,self.jack.currentToken))
            if(self.jack.tokenCat() == "IDENT"):
                self.compileSubroutineName()
            else:
                sys.exit("Invalid syntax no indentifier for subroutine at number:{} token is:{}".format(999,self.jack.currentToken))
            if(self.jack.tokenCat() == "SY_LPAREN"):
                self.eatToken()
                self.jack.advance()
            else:
                sys.exit("Invalid syntax missing ( at number:{} token is:{}".format(999,self.jack.currentToken))
            if(self.jack.tokenCat() == "KW_TYPE"):
                self.compileParameterList()
                
            if(self.jack.tokenCat() == "SY_RPAREN"):
                self.eatToken()
                self.jack.advance()
                self.compileSubroutineBody()
            else:
                sys.exit("Invalid syntax missing ) at number:{} token is:{}".format(999,self.jack.currentToken))
            
        self.closeTag("subroutineDec")    
        
    #takes care of the parameter lists
    def compileParameterList(self):
        
        self.openTag("parameterList")
        
        self.eatToken()
        self.jack.advance()
        if(self.jack.tokenCat() == "KW_TYPE"):
            self.eatToken()
            self.jack.advance()
        if(self.jack.tokenCat() == "IDENT"):
            self.eatToken()
            self.jack.advance()
        else:
            sys.exit("Invalid Syntax missing IDENT at number:{} token is:{}".format(999,self.jack.currentToken))
     #if there are multiple parameters it will consume all of them   
        while(self.jack.tokenCat() == "SY_COMMA"):
            self.eatToken()
            self.jack.advance()
            if(self.jack.tokenCat() == "KW_TYPE"):
                self.eatToken()
                self.jack.advance()
            if(self.jack.tokenCat() == "IDENT"):
                self.eatToken()
                self.jack.advance()
            else:
                sys.exit("Invalid Syntax missing IDENT at number:{} token is:{}".format(999,self.jack.currentToken))
    
        self.closeTag("parameterList")
        
    #takes care of the soubroutine body, everything in {} 
    def compileSubroutineBody(self):
        
        self.openTag("subroutineBody")
        
        if(self.jack.tokenCat() == "SY_LBRACE"):
            self.eatToken()
            self.jack.advance()
        else:
            sys.exit("Invalid Syntax missing { at number:{} token is:{}".format(999,self.jack.currentToken))
        
        if(self.jack.tokenCat() == "KW_VAR"):
            while(self.jack.tokenCat() == "KW_VAR"):
                self.compileVarDec()
        
        self.compileStatements()
        
        if(self.jack.tokenCat() =="SY_RBRACE"):
            self.eatToken()
            self.jack.advance()
        else:
            sys.exit("Invalid Syntax missing RBRACE at number:{} token is:{}".format(999,self.jack.currentToken))
            
        self.closeTag("subroutineBody")
        
    #takes care of the variable declarations in functions and methods
    def compileVarDec(self):
        self.openTag("varDec")
        
        self.eatToken()
        self.jack.advance()
        if(self.jack.tokenCat() == "KW_TYPE"):
            self.eatToken()
            self.jack.advance()
        elif(self.jack.tokenCat() == "IDENT"):
            self.compileSubroutineName()
        else:
            sys.exit("Invalid Syntax missing TYPE at number:{} token is:{}".format(999,self.jack.currentToken))
        if(self.jack.tokenCat() == "IDENT"):
            self.eatToken()
            self.jack.advance()
        else:
            sys.exit("Invalid Syntax missing IDENT at number:{} token is:{}".format(999,self.jack.currentToken))
        if(self.jack.tokenCat() == "SY_COMMA"):
            
    #While more delcarations continue eating them
            while(self.jack.tokenCat() == "SY_COMMA"):
                self.eatToken()
                self.jack.advance()
                if(self.jack.tokenCat() == "IDENT"):
                    self.eatToken()
                    self.jack.advance()
                else:
                    sys.exit("Invalid Syntax missing IDENT at number:{} token is:{}".format(999,self.jack.currentToken))
        if(self.jack.tokenCat() == "SY_SEMI"):
            self.eatToken()
            self.jack.advance()
        else:
            sys.exit("Invalid Syntax missing ; at number:{} token is:{}".format(999,self.jack.currentToken))
            
        self.closeTag("varDec")
        
    #this compiles the className
    def compileClassName(self):
        
        if(self.jack.tokenCat() == "IDENT"):
            self.eatToken()
            self.jack.advance()
        else:
            sys.exit("Invalid Syntax className at number:{} token is:{}".format(999,self.jack.currentToken))
            
    #Compiles the Subroutine Name
    def compileSubroutineName(self):
        if(self.jack.tokenCat() =="IDENT"):
            self.eatToken()
            self.jack.advance()
        else:
            sys.exit("Invalid Syntax subroutineName at number:{} token is:{}".format(999,self.jack.currentToken))
            
    #compiles the statements
    def compileStatements(self):
        self.openTag("statements")
    #While there is a statement call compile statement
        while(self.jack.currentToken in ["let","if","while","do","return"]):
            self.compileStatement()
            
        self.closeTag("statements")
        
    #Compiles statement such as let,if,do,while,return
    def compileStatement(self):
        if(self.jack.currentToken == "let"):
            self.compileLetStatement()
        elif(self.jack.currentToken == "if"):
            self.compileIfStatement()
        elif(self.jack.currentToken == "while"):
            self.compileWhileStatement()
        elif(self.jack.currentToken == "do"):
            self.compileDoStatement()
        elif(self.jack.currentToken == "return"):
            self.compileReturnStatement()
        else:
            sys.exit("Unrecognized statement at number:{} token is:{}".format(999,self.jack.currentToken))
            
    #takes care of the let statement
    def compileLetStatement(self):
        self.openTag("letStatement")
        if(self.jack.tokenCat() == "KW_LET"):
            self.eatToken()
            self.jack.advance()
            if(self.jack.tokenCat() == "IDENT"):
                self.eatToken()
                self.jack.advance()
                if(self.jack.tokenCat() == "SY_LBRACKET"):
                    self.eatToken()
                    self.jack.advance()
                    self.compileExpression()
                    if(self.jack.tokenCat() == "SY_RBRACKET"):
                        self.eatToken()
                        self.jack.advance()
                    else:
                        sys.exit("Invalid syntax expecting ] at number:{} token is:{}".format(999,self.jack.currentToken))
                if(self.jack.tokenCat() =="SY_EQ"):
                    self.eatToken()
                    self.jack.advance()
                    self.compileExpression()
                    if(self.jack.tokenCat() == "SY_SEMI"):
                        self.eatToken()
                        self.jack.advance()
    
                    else:
                        sys.exit("Invalid syntax expecting ; at number:{} token is:{}previous token is {} next token is{}".format(999,self.jack.currentToken,999,999))
                else:
                    sys.exit("Invalid syntax expecting = at number:{} token is:{}".format(999,self.jack.currentToken))
            else:
                sys.exit("Invalid syntax expecting IDENT at number:{} token is:{}".format(999,self.jack.currentToken))
        else:
            sys.exit("Invalid syntax expecting let at number:{} token is:{}".format(999,self.jack.currentToken))
        self.closeTag("letStatement")
    #takes care of if statement
    def compileIfStatement(self):
        self.openTag("ifStatement")
        if(self.jack.tokenCat() == "KW_IF"):
            self.eatToken()
            self.jack.advance()
            if(self.jack.tokenCat() =="SY_LPAREN"):
                self.eatToken()
                self.jack.advance()
                self.compileExpression()
                if(self.jack.tokenCat() == "SY_RPAREN"):
                    self.eatToken()
                    self.jack.advance()
                    
                    if(self.jack.tokenCat() == "SY_LBRACE"):
                        self.eatToken()
                        self.jack.advance()
                        self.compileStatements()
                        if(self.jack.tokenCat() == "SY_RBRACE"):
                            self.eatToken()
                            self.jack.advance()
                            if(self.jack.tokenCat() == "KW_ELSE"):
                                self.eatToken()
                                self.jack.advance()
                                if(self.jack.tokenCat() == "SY_LBRACE"):
                                    self.eatToken()
                                    self.jack.advance()
                                    self.compileStatements()
                                    if(self.jack.tokenCat() == "SY_RBRACE"):
                                        self.eatToken()
                                        self.jack.advance()
                                    else:
                                        sys.exit("Invalid syntax expecting } at number:{} token is:{}".format(999,self.jack.currentToken))
                                else:
                                    sys.exit("Invalid syntax expecting { at number:{} token is:{}".format(999,self.jack.currentToken))
                        else:
                            sys.exit("Invalid syntax expecting RBRACE at number:{} token is:{}".format(999,self.jack.currentToken))
                else:
                    sys.exit("Invalid syntax expecting ) at number:{} token is:{}".format(999,self.jack.currentToken))
            else:
                sys.exit("Invalid syntax expecting ( at number:{} token is:{}".format(999,self.jack.currentToken))
        else:
            sys.exit("Invalid syntax expecting if at number:{} token is:{}".format(999,self.jack.currentToken))
        self.closeTag("ifStatement")
    #compiles while statement
    def compileWhileStatement(self):
        self.openTag("whileStatement")
        if(self.jack.tokenCat() == "KW_WHILE"):
            self.eatToken()
            self.jack.advance()
            if(self.jack.tokenCat() == "SY_LPAREN"):
                self.eatToken()
                self.jack.advance()
                self.compileExpression()
                if(self.jack.tokenCat() == "SY_RPAREN"):
                    self.eatToken()
                    self.jack.advance()
                    if(self.jack.tokenCat() =="SY_LBRACE"):
                        self.eatToken()
                        self.jack.advance()
                        
                        self.compileStatements()
                        if(self.jack.tokenCat() == "SY_RBRACE"):
                            self.eatToken()
                            self.jack.advance()
                        else:
                            sys.exit("Invalid syntax expecting RBRACE at number:{} token is:{}".format(999,self.jack.currentToken))
                    else:
                        sys.exit("Invalid syntax expecting { at number:{} token is:{}".format(999,self.jack.currentToken))
                else:
                    sys.exit("Invalid syntax expecting ) at number:{} token is:{}".format(999,self.jack.currentToken))
            else:
                sys.exit("Invalid syntax expecting ( at number:{} token is:{}".format(999,self.jack.currentToken))
        else:
            sys.exit("Invalid syntax expecting while at number:{} token is:{}".format(999,self.jack.currentToken))
        self.closeTag("whileStatement")
        
    #compiles DO statement
    def compileDoStatement(self):
        self.openTag("doStatement")
        if(self.jack.tokenCat() == "KW_DO"):
            self.eatToken()
            self.jack.advance()
            self.compileSubroutineCall()
            if(self.jack.tokenCat() =="SY_SEMI"):
                self.eatToken()
                self.jack.advance()
            else:
                sys.exit("Invalid syntax expecting ; at number:{} token is:{}".format(999,self.jack.currentToken))
        else:
            sys.exit("Invalid syntax expecting DO at number:{} token is:{}".format(999,self.jack.currentToken))
        self.closeTag("doStatement")
        
    #Compiles return statement
    def compileReturnStatement(self):
        self.openTag("returnStatement")
        if(self.jack.tokenCat() == "KW_RETURN"):
            self.eatToken()
            self.jack.advance()
        
            if(self.jack.tokenCat() == "SY_SEMI"):
                self.eatToken()
                self.jack.advance()
            else:
                self.compileExpression()
                if(self.jack.tokenCat() == "SY_SEMI"):
                    self.eatToken()
                    self.jack.advance()
                else:
                    sys.exit("Invalid syntax expecting ; at number:{} token is:{}".format(999,self.jack.currentToken))
        else:
            sys.exit("Invalid syntax expecting return at number:{} token is:{}".format(999,self.jack.currentToken))
        self.closeTag("returnStatement")
        
    #compiles an expression
    def compileExpression(self):
        self.openTag("expression")
        self.compileTerm()
    
        if(self.jack.currentToken in self.operators):
            while(self.jack.currentToken in self.operators):
                self.eatToken()
                self.jack.advance()
                self.compileTerm()
        self.closeTag("expression")
    
    #compiles a term
    def compileTerm(self):
        self.openTag("term")
    
        if(self.jack.tokenCat() =="INTEGER"):
            self.eatToken()
            self.jack.advance()
        if(self.jack.tokenCat() =="STRING"):
            self.eatToken()
            self.jack.advance()
        if(self.jack.currentToken in self.keyWords):
            self.eatToken()
            self.jack.advance()
        if(self.jack.tokenCat() == "IDENT"):
            self.eatToken()
            self.jack.advance()
            if(self.jack.tokenCat() == "SY_PERIOD"):
                self.compileSubroutineCall()
                          
            if(self.jack.tokenCat() == "SY_LBRACKET"):
                self.eatToken()
                self.jack.advance()
                self.compileExpression()
                if(self.jack.tokenCat() == "SY_RBRACKET"):
                    self.eatToken()
                    self.jack.advance()
                else:
                    sys.exit("Invalid syntax expecting ] at number:{} token is:{}".format(999,self.jack.currentToken))
        if(self.jack.tokenCat() =="SY_LPAREN"):
            self.eatToken()
            self.jack.advance()
            self.compileExpression()
            if(self.jack.tokenCat() == "SY_RPAREN"):
                self.eatToken()
                self.jack.advance()
            else:
                sys.exit("Invalid syntax expecting ) at number:{} token is:{}".format(999,self.jack.currentToken))
        if(self.jack.currentToken in self.unops):
            self.eatToken()
            self.jack.advance()
            self.compileTerm()
    
        self.closeTag("term")
    
    #takes care of the subroutine call
    def compileSubroutineCall(self):
        if(self.jack.tokenCat() == "SY_PERIOD"):
            self.eatToken()
            self.jack.advance()
        if(self.jack.tokenCat() == "IDENT"):
            self.compileSubroutineName()
        else:
            sys.exit("Invalid syntax expecting subroutineName at number:{} token is:{}".format(999,self.jack.currentToken))
        if(self.jack.tokenCat() == "SY_LPAREN"):
            self.eatToken()
            self.jack.advance()
            self.compileExpressionList()
            if(self.jack.tokenCat() == "SY_RPAREN"):
                self.eatToken()
                self.jack.advance()
            else:
                sys.exit("Invalid syntax expecting ) at number:{} token is:{}".format(999,self.jack.currentToken))
        elif(self.jack.tokenCat() == "SY_PERIOD"):
            self.eatToken()
            self.jack.advance()
            self.compileSubroutineName()
            if(self.jack.tokenCat() =="SY_LPAREN"):
                self.eatToken()
                self.jack.advance()
            else:
                sys.exit("Invalid syntax expecting ( at number:{} token is:{}".format(999,self.jack.currentToken))
            self.compileExpressionList()
            if(self.jack.tokenCat() == "SY_RPAREN"):
                self.eatToken()
                self.jack.advance()
            else:
                sys.exit("Invalid syntax expecting ) at number:{} token is:{}".format(999,self.jack.currentToken))
            
        else:
            sys.exit("Invalid syntax expecting ( or . at number:{} token is:{}".format(999,self.jack.currentToken))
        self.compileExpressionList()
        
    #takes care of a list of expressions
    def compileExpressionList(self):
        self.openTag("expressionList")
        self.compileExpression()
        if(self.jack.tokenCat() == "SY_COMMA"):
            while(self.jack.tokenCat() == "SY_COMMA"):
                self.eatToken()
                self.jack.advance()
                self.compileExpression()
        self.closeTag("expressionList")
    
    #Opens a recursive tag, example 
    #<class>
    #stuff 
    #stuff
    #</class>
    def openTag(self,tagName):
         self.outFile.write("\n<{}>".format(tagName))
    #This is the closing tag for classes and functions
    def closeTag(self,tagName):
        self.outFile.write("\n</{}>".format(tagName))
    #This takes the token and write it to the file moving to the next token always only looking at the current token
    def eatToken(self):
        
        if(self.jack.currentToken in self.keyWords):
            self.outFile.write("\n<{}> {} </{}>".format("keyword",self.jack.currentToken,"keyword"))
        elif(self.jack.currentToken in self.symbols):
            if(self.jack.currentToken == "<"):
                self.outFile.write("\n<{}> {} </{}>".format("symbol","&lt;","symbol"))
            elif(self.jack.currentToken == ">"):
                self.outFile.write("\n<{}> {} </{}>".format("symbol","&gt;","symbol"))
            elif(self.jack.currentToken == "&"):
                self.outFile.write("\n<{}> {} </{}>".format("symbol","&amp;","symbol"))
            else:
                self.outFile.write("\n<{}> {} </{}>".format("symbol",self.jack.currentToken,"symbol"))
        elif(self.jack.tokenCat() =="IDENT"):
            self.outFile.write("\n<{}> {} </{}>".format("identifier",self.jack.currentToken,"identifier"))
        elif(self.jack.tokenCat() =="INTEGER"):
            self.outFile.write("\n<{}> {} </{}>".format("integerConstant",self.jack.currentToken,"integerConstant"))
        elif(self.jack.tokenCat() == "STRING"):
            self.outFile.write("\n<{}> {} </{}>".format("stringConstant",self.jack.currentToken.replace("\"", ''),"stringConstant"))
        else:    
            self.outFile.write("\n<{}> {} </{}>".format(self.jack.tokenCat(),self.jack.currentToken,self.jack.tokenCat()))
    
    
comp = CompilationEngine("Main.jack")
