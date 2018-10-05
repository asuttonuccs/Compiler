
//PUSH CONST
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//PUSH CONST
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//EQ
@SP
AM=M-1
D=M
A=A-1
D=M-D
@EQ.true.0
D;JEQ
@SP
A=M-1
M=0
@EQ.follow.0
0;JMP
(EQ.true.0)
@SP
A=M-1
M=-1
(EQ.follow.0)

//PUSH CONST
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//PUSH CONST
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

//EQ
@SP
AM=M-1
D=M
A=A-1
D=M-D
@EQ.true.1
D;JEQ
@SP
A=M-1
M=0
@EQ.follow.1
0;JMP
(EQ.true.1)
@SP
A=M-1
M=-1
(EQ.follow.1)

//PUSH CONST
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

//PUSH CONST
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//EQ
@SP
AM=M-1
D=M
A=A-1
D=M-D
@EQ.true.2
D;JEQ
@SP
A=M-1
M=0
@EQ.follow.2
0;JMP
(EQ.true.2)
@SP
A=M-1
M=-1
(EQ.follow.2)

//PUSH CONST
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

//PUSH CONST
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//LT
@SP
AM=M-1
D=M
A=A-1
D=M-D
@LT.true.3
D;JLT
@SP
A=M-1
M=0
@LT.follow.3
0;JMP
(LT.true.3)
@SP
A=M-1
M=-1
(LT.follow.3)

//PUSH CONST
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//PUSH CONST
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

//LT
@SP
AM=M-1
D=M
A=A-1
D=M-D
@LT.true.4
D;JLT
@SP
A=M-1
M=0
@LT.follow.4
0;JMP
(LT.true.4)
@SP
A=M-1
M=-1
(LT.follow.4)

//PUSH CONST
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//PUSH CONST
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//LT
@SP
AM=M-1
D=M
A=A-1
D=M-D
@LT.true.5
D;JLT
@SP
A=M-1
M=0
@LT.follow.5
0;JMP
(LT.true.5)
@SP
A=M-1
M=-1
(LT.follow.5)

//PUSH CONST
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

//PUSH CONST
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//GT
@SP
AM=M-1
D=M
A=A-1
D=M-D
@GT.true.6

D;JGT
@SP
A=M-1
M=0
@GT.follow.6
0;JMP
(GT.true.6)
@SP
A=M-1
M=-1
(GT.follow.6)

//PUSH CONST
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//PUSH CONST
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

//GT
@SP
AM=M-1
D=M
A=A-1
D=M-D
@GT.true.7

D;JGT
@SP
A=M-1
M=0
@GT.follow.7
0;JMP
(GT.true.7)
@SP
A=M-1
M=-1
(GT.follow.7)

//PUSH CONST
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//PUSH CONST
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//GT
@SP
AM=M-1
D=M
A=A-1
D=M-D
@GT.true.8

D;JGT
@SP
A=M-1
M=0
@GT.follow.8
0;JMP
(GT.true.8)
@SP
A=M-1
M=-1
(GT.follow.8)

//PUSH CONST
@57
D=A
@SP
A=M
M=D
@SP
M=M+1

//PUSH CONST
@31
D=A
@SP
A=M
M=D
@SP
M=M+1

//PUSH CONST
@53
D=A
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

//PUSH CONST
@112
D=A
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

//NEG
@SP
A=M-1
M=-M

//AND
@SP
AM=M-1
D=M
A=A-1
M=D&M

//PUSH CONST
@82
D=A
@SP
A=M
M=D
@SP
M=M+1

//OR
@SP
AM=M-1
D=M
A=A-1
M=D|M

//NOT
@SP
A=M-1
M=!M
