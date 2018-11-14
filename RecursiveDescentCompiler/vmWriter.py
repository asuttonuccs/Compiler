# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:05:39 2018

@author: Adric
"""

class VMWriter():
    def __init__(self, file):
        self.output = open(file, 'w')
        self.commandDict = {'+':"add\n", '-':"sub\n",'*':"call Math.multiply 2\n", '/':"call Mat.divide 2\n", '&':"and\n", '|':"or\n",'<':"lt\n", '>':"gt\n", '=':"eq\n", 'neg':"neg\n"}
    def writePush(self, segment, index):
        self.output.write("push {} {}\n".format(segment, index))
    def writePop(self, segment, index):
        self.output.write("pop {} {}\n".format(segment, index))
    def writeArithmetic(self, command):
        if command in self.commandDict:
            self.output.write(self.commandDict[command])
    def writeLabel(self, label):
        self.output.write("label {}\n".format(label))
    def writeGoto(self, label):
        self.output.write("goto {}\n".format(label))
    def writeIf(self, label):
        self.output.write("if-goto {}\n".format(label))
    def writeCall(self, name, n_args):
        self.output.write("call {} {}\n".format(name, n_args))
    def writeFunction(self, name, n_locals):
        self.output.write("function {} {}\n".format(name, n_locals))
    def writeReturn(self):
        self.output.write("return\n")
    def close(self):
        self.output.close()
    
#vm = VMWriter("write_test.txt")
#vm.writePush("local",2)
#vm.writePop("arg",3)
#vm.writeArithmetic("*")
#vm.writeLabel("lab2")
#vm.writeCall("run",1)
#vm.writeFunction("freeStuff",2)
#vm.writeReturn()
#vm.close()