
//PUSH CONST
@111
D=A
@SP
A=M
M=D
@SP
M=M+1

//PUSH CONST
@333
D=A
@SP
A=M
M=D
@SP
M=M+1

//PUSH CONST
@888
D=A
@SP
A=M
M=D
@SP
M=M+1

//POP STATIC
@StaticTest.asm.8
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

//POP STATIC
@StaticTest.asm.3
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

//POP STATIC
@StaticTest.asm.1
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

//PUSH STATIC
@StaticTest.asm.3
D=M
@SP
A=M
M=D
@SP
M=M+1

//PUSH STATIC
@StaticTest.asm.1
D=M
@SP
A=M
M=D
@SP
M=M+1

//SUB
@SP
AM=M-1
D=M
A=A-1
M=M-D

//PUSH STATIC
@StaticTest.asm.8
D=M
@SP
A=M
M=D
@SP
M=M+1

//ADD
@SP
AM=M-1
D=M
A=A-1
M=D+M
