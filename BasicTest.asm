
//PUSH CONST
@10
D=A
@SP
A=M
M=D
@SP
M=M+1

//POP LCL
@LCL
D=M
@0
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

//PUSH CONST
@21
D=A
@SP
A=M
M=D
@SP
M=M+1

//PUSH CONST
@22
D=A
@SP
A=M
M=D
@SP
M=M+1

//POP ARG
@ARG
D=M
@2
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

//POP ARG
@ARG
D=M
@1
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

//PUSH CONST
@36
D=A
@SP
A=M
M=D
@SP
M=M+1

//POP THIS
@THIS
D=M
@6
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

//PUSH CONST
@42
D=A
@SP
A=M
M=D
@SP
M=M+1

//PUSH CONST
@45
D=A
@SP
A=M
M=D
@SP
M=M+1

//POP THAT
@THAT
D=M
@5
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

//POP THAT
@THAT
D=M
@2
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

//PUSH CONST
@510
D=A
@SP
A=M
M=D
@SP
M=M+1
@R5
D=A
@6
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

//PUSH LCL
@LCL
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

//PUSH THAT
@THAT
D=M
@5
A=D+A
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

//PUSH ARG
@ARG
D=M
@1
A=D+A
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

//PUSH THIS
@THIS
D=M
@6
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

//PUSH THIS
@THIS
D=M
@6
A=D+A
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

//SUB
@SP
AM=M-1
D=M
A=A-1
M=M-D

//PUSH TEMP
@R5
D=A
@6
A=D+A
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
