# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 08:50:44 2018

@author: Adric
"""

class SymbolTable():
    def __init__(self):
        self.global_table = {}
        self.local_table = {}
        self.global_static_index = 0
        self.global_field_index = 0
        self.local_arg_index = 0
        self.local_var_index = 0
    
    def startSubroutine(self):
        self.local_table.clear()
        self.local_arg_index = 0
        self.local_var_index = 0
        
        
    def define(self, name, symbol_type, kind):
        if(kind) == "static":
            self.global_table[name] = (symbol_type, kind, self.global_static_index)
            self.global_static_index += 1
        elif(kind) == "field":
            self.global_table[name] = (symbol_type, kind, self.global_field_index)
            self.global_field_index += 1
        elif(kind) == "arg":
            self.local_table[name] = (symbol_type, kind, self.local_arg_index)
            self.local_arg_index += 1
        elif(kind) == "var":
            self.local_table[name] = (symbol_type, kind, self.local_var_index)
            self.local_var_index +=1
    
    #symbol[1] is the kind of the entry [var,static,field,arg]
    def varCount(self, kind):
        count = 0
        for symbol in self.local_table.values():
            if symbol[1] == kind:
                count += 1
        for symbol in self.global_table.values():
            if symbol[1] == kind:
                count +=1
        return count
    def kindOf(self,name):
        if(name) in self.local_table:
            return self.local_table[name][1]
        if(name) in self.global_table:
            return self.global_table[name][1]
        return None
    def typeOf(self,name):
        if(name) in self.local_table:
            return self.local_table[name][0]
        if(name) in self.global_table:
            return self.global_table[name][0]
        return None
    def indexOf(self,name):
        if(name) in self.local_table:
            return self.local_table[name][2]
        if(name) in self.global_table:
            return self.global_table[name][2]
        return None
    
#sym = SymbolTable()
#sym.define("Fred", "ident", "var")
#sym.define("Bob", "ident", "arg")
#sym.define("C", "ident", "static")
#sym.define("D", "ident", "field")
#sym.define("Ted", "ident", "var")
#sym.define("Brad", "ident", "var")
#
#print(sym.global_table)
#print(sym.local_table)
#print(sym.varCount("var"))
#print(sym.local_table.values())
#print(sym.kindOf("Fred"))
#print(sym.typeOf("Fred"))
#print(sym.indexOf("Brad"))