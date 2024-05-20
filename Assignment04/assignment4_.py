import numpy as np
import random
################################################


########### HELPER FUNCTIONS ###############
def String_to_List(s):
    a=[]
    for i in s:
        a.append(int(i))
    return a

def List_to_String(a):
    s=str()
    for i in a:
        s+=str(i)
    return s


def Binary_to_Int(s):
    return int(s,2)


def Int_to_Binary(n):
    return f'{n:08b}'


def String_to_Binary(s):
    s1=''.join(format(ord(i), '08b') for i in s)
    return String_to_List(s1)


def IP(s_):
    s=List_to_String(s_)

    s1=s[57]+s[49]+s[41]+s[33]+s[25]+s[17]+s[9]+s[1]+s[59]+s[51]+s[43]+s[35]+s[27]+s[19]+s[11]+s[3]+s[61]+s[53]+s[45]+s[37]+s[29]+s[21]+s[13]+s[5]+s[63]+s[55]+s[47]+s[39]+s[31]+s[23]+s[15]+s[7]+s[56]+s[48]+s[40]+s[32]+s[24]+s[16]+s[8]+s[0]+s[58]+s[50]+s[42]+s[34]+s[26]+s[18]+s[10]+s[2]+s[60]+s[52]+s[44]+s[36]+s[28]+s[20]+s[12]+s[4]+s[62]+s[54]+s[46]+s[38]+s[30]+s[22]+s[14]+s[6]
    return String_to_List(s1)


def IP_inverse(s_):
    s=List_to_String(s_)
    s2=s[39]+s[7]+s[47]+s[15]+s[55]+s[23]+s[63]+s[31]+s[38]+s[6]+s[46]+s[14]+s[54]+s[22]+s[62]+s[30]+s[37]+s[5]+s[45]+s[13]+s[53]+s[21]+s[61]+s[29]+s[36]+s[4]+s[44]+s[12]+s[52]+s[20]+s[60]+s[28]+s[35]+s[3]+s[43]+s[11]+s[51]+s[19]+s[59]+s[27]+s[34]+s[2]+s[42]+s[10]+s[50]+s[18]+s[58]+s[26]+s[33]+s[1]+s[41]+s[9]+s[49]+s[17]+s[57]+s[26]+s[32]+s[0]+s[40]+s[8]+s[48]+s[16]+s[56]+s[24]
    return String_to_List(s2)

def REP(s):
    s=List_to_String(s)
    s1=s[7]+s[39]+s[15]+s[47]+s[23]+s[55]+s[31]+s[63]+s[6]+s[38]+s[14]+s[46]+s[22]+s[54]+s[30]+s[62]+s[5]+s[37]+s[13]+s[45]+s[21]+s[53]+s[29]+s[61]+s[4]+s[36]+s[12]+s[44]+s[20]+s[52]+s[28]+s[60]+s[3]+s[35]+s[11]+s[43]+s[19]+s[51]+s[27]+s[59]+s[2]+s[34]+s[10]+s[42]+s[18]+s[50]+s[26]+s[58]+s[1]+s[33]+s[9]+s[41]+s[17]+s[49]+s[25]+s[57]+s[0]+s[32]+s[8]+s[40]+s[16]+s[48]+s[24]+s[56]
    return String_to_List(s1)

def REP_inverse(s):
    s=List_to_String(s)
    s2=s[56]+s[48]+s[40]+s[32]+s[24]+s[16]+s[8]+s[0]+s[58]+s[50]+s[42]+s[34]+s[26]+s[18]+s[10]+s[2]+s[60]+s[52]+s[44]+s[36]+s[28]+s[20]+s[12]+s[4]+s[62]+s[54]+s[46]+s[38]+s[30]+s[22]+s[14]+s[6]+s[57]+s[49]+s[41]+s[33]+s[25]+s[17]+s[9]+s[1]+s[59]+s[51]+s[43]+s[35]+s[27]+s[19]+s[11]+s[3]+s[61]+s[53]+s[45]+s[37]+s[29]+s[21]+s[13]+s[5]+s[63]+s[55]+s[47]+s[39]+s[31]+s[23]+s[15]+s[7]
    return String_to_List(s2)


def ApplySblock(s_):

    s=List_to_String(s_)

    P=str()
    p11=s[0]+s[5]
    p11_=Binary_to_Int(p11)
    p12=s[1:5]
    p12_=Binary_to_Int(p12)
    p21=s[6]+s[11]
    p21_=Binary_to_Int(p21)
    p22=s[7:11]
    p22_=Binary_to_Int(p22)
    p31=s[12]+s[17]
    p31_=Binary_to_Int(p31)
    p32=s[13:17]
    p32_=Binary_to_Int(p32)
    p41=s[18]+s[23]
    p41_=Binary_to_Int(p41)
    p42=s[19:23]
    p42_=Binary_to_Int(p42)
    p51=s[24]+s[29]
    p51_=Binary_to_Int(p51)
    p52=s[25:29]
    p52_=Binary_to_Int(p52)
    p61=s[30]+s[35]
    p61_=Binary_to_Int(p61)
    p62=s[31:35]
    p62_=Binary_to_Int(p62)
    p71=s[36]+s[41]
    p71_=Binary_to_Int(p71)
    p72=s[37:41]
    p72_=Binary_to_Int(p72)
    p81=s[42]+s[47]
    p81_=Binary_to_Int(p81)
    p82=s[43:47]
    p82_=Binary_to_Int(p82)

    s1=[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
    s2=[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
    s3=[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
    s4=[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]
    s5=[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
    s6=[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]
    s7=[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
    s8=[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]


    P=str(Int_to_Binary(s1[p11_][p12_]))[4:8]+str(Int_to_Binary(s2[p21_][p22_]))[4:8]+str(Int_to_Binary(s3[p31_][p32_]))[4:8]+str(Int_to_Binary(s4[p41_][p42_]))[4:8]+str(Int_to_Binary(s5[p51_][p52_]))[4:8]+str(Int_to_Binary(s6[p61_][p62_]))[4:8]+str(Int_to_Binary(s7[p71_][p72_]))[4:8]+str(Int_to_Binary(s8[p81_][p82_]))[4:8]

    return String_to_List(P)

def S1(s_):
    s=List_to_String(s_)
    s1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
          [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
          [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
    p11 = s[0] + s[5]
    p11_ = Binary_to_Int(p11)
    p12 = s[1:5]
    p12_ = Binary_to_Int(p12)

    P = str(Int_to_Binary(s1[p11_][p12_]))[4:8]

    return String_to_List(P)

def S2(s_):
    s = List_to_String(s_)
    s2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
          [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
          [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
          [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

    p11 = s[0] + s[5]
    p11_ = Binary_to_Int(p11)
    p12 = s[1:5]
    p12_ = Binary_to_Int(p12)

    P = str(Int_to_Binary(s2[p11_][p12_]))[4:8]

    return String_to_List(P)

def S3(s_):
    s = List_to_String(s_)
    s3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
          [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
          [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
          [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]

    p11 = s[0] + s[5]
    p11_ = Binary_to_Int(p11)
    p12 = s[1:5]
    p12_ = Binary_to_Int(p12)

    P = str(Int_to_Binary(s3[p11_][p12_]))[4:8]

    return String_to_List(P)

def S4(s_):
    s = List_to_String(s_)
    s4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
          [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
          [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
          [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

    p11 = s[0] + s[5]
    p11_ = Binary_to_Int(p11)
    p12 = s[1:5]
    p12_ = Binary_to_Int(p12)

    P = str(Int_to_Binary(s4[p11_][p12_]))[4:8]

    return String_to_List(P)

def S5(s_):
    s = List_to_String(s_)
    s5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
          [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
          [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
          [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

    p11 = s[0] + s[5]
    p11_ = Binary_to_Int(p11)
    p12 = s[1:5]
    p12_ = Binary_to_Int(p12)

    P = str(Int_to_Binary(s5[p11_][p12_]))[4:8]

    return String_to_List(P)

def S6(s_):
    s = List_to_String(s_)
    s6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
          [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
          [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
          [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]

    p11 = s[0] + s[5]
    p11_ = Binary_to_Int(p11)
    p12 = s[1:5]
    p12_ = Binary_to_Int(p12)

    P = str(Int_to_Binary(s6[p11_][p12_]))[4:8]

    return String_to_List(P)

def S7(s_):
    s = List_to_String(s_)
    s7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
          [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
          [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
          [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

    p11 = s[0] + s[5]
    p11_ = Binary_to_Int(p11)
    p12 = s[1:5]
    p12_ = Binary_to_Int(p12)

    P = str(Int_to_Binary(s7[p11_][p12_]))[4:8]

    return String_to_List(P)


def S8(s_):
    s = List_to_String(s_)
    s8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
          [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
          [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
          [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

    p11 = s[0] + s[5]
    p11_ = Binary_to_Int(p11)
    p12 = s[1:5]
    p12_ = Binary_to_Int(p12)

    P = str(Int_to_Binary(s8[p11_][p12_]))[4:8]

    return String_to_List(P)



# 32_digit input
def Expansion(s_):
    s = List_to_String(s_)
    s1=s[31]+s[0]+s[1]+s[2]+s[3]+s[4]+s[3]+s[4]+s[5]+s[6]+s[7]+s[8]+s[7]+s[8]+s[9]+s[10]+s[11]+s[12]+s[11]+s[12]+s[13]+s[14]+s[15]+s[16]+s[15]+s[16]+s[17]+s[18]+s[19]+s[20]+s[19]+s[20]+s[21]+s[22]+s[23]+s[24]+s[23]+s[24]+s[25]+s[26]+s[27]+s[28]+s[27]+s[28]+s[29]+s[30]+s[31]+s[0]
    return String_to_List(s1)

# 32_digit input
def Permutation(s_):
    s = List_to_String(s_)
    s1=s[15]+s[6]+s[19]+s[20]+s[28]+s[11]+s[27]+s[16]+s[0]+s[14]+s[22]+s[25]+s[4]+s[17]+s[30]+s[9]+s[1]+s[7]+s[23]+s[13]+s[31]+s[26]+s[2]+s[8]+s[18]+s[12]+s[29]+s[5]+s[21]+s[10]+s[3]+s[24]
    return String_to_List(s1)

# 32_1digit input
def Permutationinverse(s_):
    s = List_to_String(s_)
    s1=s[8]+s[16]+s[22]+s[30]+s[12]+s[27]+s[1]+s[17]+s[23]+s[15]+s[29]+s[5]+s[25]+s[19]+s[9]+s[0]+s[7]+s[13]+s[24]+s[2]+s[3]+s[28]+s[10]+s[18]+s[31]+s[11]+s[21]+s[6]+s[4]+s[26]+s[14]+s[20]
    return String_to_List(s1)

#x=np.concatenate(([1],[0]*47))
#print(Permutationinverse(Permutation(x)))

B=[]
def generateB(arr,l):
    if len(arr)==l:
        arr=[int(i) for i in arr]
        B.append(arr)
        return
    t=list(np.concatenate((arr,[int(1)])))
    generateB(t,l)
    t_=list(np.concatenate((arr,[int(0)])))
    generateB(t_,l)
generateB([],6)


def Converttostring(arr):
    ans=""
    for i in arr:
        ans=ans+str(i)
    return ans


def Xor(a,b):
    ans=[]
    for i in range(len(a)):
        a_,b_=a[i],b[i]
        if a_==b_:
            ans.append(0)
        else :
            ans.append(1)
    return ans

######################################################################
#### Solve for a specific block a,a_=input to that specific block############### 
def solveforoneblock(a,a_,outputxor_,block):
    key=[]
    outputxor=Converttostring(outputxor_)
    if block==1:
        for i in B:
            key_a=Xor(a,i)
            key_a_=Xor(a_,i)
            if outputxor==Converttostring(Xor(S1(key_a),S1(key_a_))):
                key.append(i)
    if block==2:
        for i in B:
            key_a=Xor(a,i)
            key_a_=Xor(a_,i)
            if outputxor==Converttostring(Xor(S2(key_a),S2(key_a_))):
                key.append(i)
    if block==3:
        for i in B:
            key_a=Xor(a,i)
            key_a_=Xor(a_,i)
            if outputxor==Converttostring(Xor(S3(key_a),S3(key_a_))):
                key.append(i)
    if block==4:
        for i in B:
            key_a=Xor(a,i)
            key_a_=Xor(a_,i)
            if outputxor==Converttostring(Xor(S4(key_a),S4(key_a_))):
                key.append(i)
    if block==5:
        for i in B:
            key_a=Xor(a,i)
            key_a_=Xor(a_,i)
            if outputxor==Converttostring(Xor(S5(key_a),S5(key_a_))):
                key.append(i)
    if block==6:
        for i in B:
            key_a=Xor(a,i)
            key_a_=Xor(a_,i)
            if outputxor==Converttostring(Xor(S6(key_a),S6(key_a_))):
                key.append(i)
    if block==7:
        for i in B:
            key_a=Xor(a,i)
            key_a_=Xor(a_,i)
            if outputxor==Converttostring(Xor(S7(key_a),S7(key_a_))):
                key.append(i)
    if block==8:
        for i in B:
            key_a=Xor(a,i)
            key_a_=Xor(a_,i)
            if outputxor==Converttostring(Xor(S8(key_a),S8(key_a_))):
                key.append(i)
    return key
############Calculating Output Xor for a specific block############
############ R1,R2 is the right half of cipher text, ###########
######## a will the the r-2 characteristic left half ############
def caloutputxorforblock(R1,R2,block,a):
    X=Permutationinverse(Xor(Xor(R1,R2),a))
    return X[(block-1)*4:block*4]
############## basically does expansion so solveforoneblock can be applied########

def calculateinputforblock(L,block):
    exp=Expansion(L)
    return exp[(block-1)*6:block*6]
######## t will the the r-2 characteristic left half ############
def findkeysforonepaironespecificblock(R1,R2,L1,L2,block,t):
    a=calculateinputforblock(L1,block)
    _a=calculateinputforblock(L2,block)
    outputxor_=caloutputxorforblock(R1,R2,block,t)
    key=solveforoneblock(a,_a,outputxor_,block)
    return key
######## t will the the r-2 characteristic left half ############
######### blocks are possible blocks for thoes you want to find the key##########
def findindingkeysforaspecificpair(C1,C2,blocks,t):
    L1=C1[0:32]
    L2=C2[0:32]
    R1=C1[32:]
    R2=C2[32:]
    d=dict()
    if 1 in blocks:
        d[1]=findkeysforonepaironespecificblock(R1,R2,L1,L2,1,t)
    if 2 in blocks:
        d[2]=findkeysforonepaironespecificblock(R1,R2,L1,L2,2,t)
    if 3 in blocks:
        d[3]=findkeysforonepaironespecificblock(R1,R2,L1,L2,3,t)
    if 4 in blocks:
        d[4]=findkeysforonepaironespecificblock(R1,R2,L1,L2,4,t)
    if 5 in blocks:
        d[5]=findkeysforonepaironespecificblock(R1,R2,L1,L2,5,t)
    if 6 in blocks:
        d[6]=findkeysforonepaironespecificblock(R1,R2,L1,L2,6,t)
    if 7 in blocks:
        d[7]=findkeysforonepaironespecificblock(R1,R2,L1,L2,7,t)
    if 8 in blocks:
        d[8]=findkeysforonepaironespecificblock(R1,R2,L1,L2,8,t)
    return d
####### generate an array for all blocks ##########
def findforallpairs(C,blocks,t):
    arr=[]
    for i in range(0,len(C),2):
        arr.append(findindingkeysforaspecificpair(C[i],C[i+1],blocks,t))
    return arr
def findingvalidkeysforablock(arr_arr,p,l):
    # make an arr of distinct keys
    diskey=[]
    for i in arr_arr:
        for j in i:
            if j not in diskey:
                diskey.append(j)
 ###   count of each key ####
    count=[]
    for i in diskey:
        count_=0
        for j in arr_arr:
            if i in j:
                count_=count_+1
        count.append(count_)
###### finally make the valid dictionary having count as keys and possible keys as values
    d=dict()
    d["arr"]=diskey
    d["count"]=count
    ''' for i in range(len(count)):
            if count[i] not in d.keys():
                d[count[i]]=list()
            t=d[count[i]]
            t.append(diskey[i])
            d[count[i]]=t'''
    return d
############# p is the probablity ############
################ t is the characteristics of r-2 ########
########### blocks an array of S blocks that are having 0 input Xor #####  
def seperatealldata(C,blocks,t,p):
    ans=dict()
    l=len(C)/2
    arr_dic=findforallpairs(C,blocks,t)
    if 1 in arr_dic[0].keys():
        arr_arr=[]
        for i in arr_dic:
            arr_arr.append(i[1])
        ans[1]=findingvalidkeysforablock(arr_arr,p,l)
    if 2 in arr_dic[0].keys():
        arr_arr=[]
        for i in arr_dic:
            arr_arr.append(i[2])
        ans[2]=findingvalidkeysforablock(arr_arr,p,l)
    if 3 in arr_dic[0].keys():
        arr_arr=[]
        for i in arr_dic:
            arr_arr.append(i[3])
        ans[3]=findingvalidkeysforablock(arr_arr,p,l)
    if 4 in arr_dic[0].keys():
        arr_arr=[]
        for i in arr_dic:
            arr_arr.append(i[4])
        ans[4]=findingvalidkeysforablock(arr_arr,p,l)
    if 5 in arr_dic[0].keys():
        arr_arr=[]
        for i in arr_dic:
            arr_arr.append(i[5])
        ans[5]=findingvalidkeysforablock(arr_arr,p,l)
    if 6 in arr_dic[0].keys():
        arr_arr=[]
        for i in arr_dic:
            arr_arr.append(i[6])
        ans[6]=findingvalidkeysforablock(arr_arr,p,l)
    if 7 in arr_dic[0].keys():
        arr_arr=[]
        for i in arr_dic:
            arr_arr.append(i[7])
        ans[7]=findingvalidkeysforablock(arr_arr,p,l)
    if 8 in arr_dic[0].keys():
        arr_arr=[]
        for i in arr_dic:
            arr_arr.append(i[8])
        ans[8]=findingvalidkeysforablock(arr_arr,p,l)
    return ans

###############################################################





###########################################################
def generateonerandomplaintext():
    ans=[]
    for i in range(64):
        ans.append(random.randint(0,1))
    return ans
def generatePlaintextpairs(a,number):
    P=[]
    a_=IP_inverse(a)
    count=0
    while len(P)/2 < number:
        x=generateonerandomplaintext()
        x1=Xor(x,a_)
        count=count+1
        if x in P or x1 in P:
            continue
        else:
            P.append(x)
            P.append(x1)
        if count>=number*3:
            print("not able to generate "+(len(P)/2))
            break
    return P
def generateFile(P,suf):
    Pwords=makearrPintotext(P)
    filename="plaintext"+str(suf)+".txt"
    file=open(filename,"w")
    file.write("NAA\nNAA\n4\nread\n")
    for i in Pwords:
        file.write(i+"\n")
        file.write("c\n")
    file.close()
    return


def Text_to_Bits(s):
    P=str()
    for i in s:
        x=ord(i)-ord("f")
        y=str(f'{x:08b}')[4:8]
        P+=y
    return String_to_List(P)

def Bits_to_Text(q):
    P=List_to_String(q)
    R=str()
    for i in range(0,len(P),4):
        x=P[i:i+4]
        y=int(x,2)
        R+=chr(y+ord("f"))

    return Converttostring(list(R))

def makearrPintotext(P):
    ans=[]
    for i in P:
        ans.append(Bits_to_Text(i))
    return ans
def makearrCintobits(C):
    ans=[]
    for i in C:
        ans.append(REP_inverse(Text_to_Bits(i)))  ############
    return ans

def readfile(loc):
    C=[]
    file=open(loc)
    for i in file:
        C.append(i[0:16])
    return C

####################################################################3



def spe (arr,count):
    avg=np.average(count)
    l=list()
    print(avg)
    for i in range(len(arr)):
        key=arr[i]
        count_=count[i]
        if count_ >= 2*avg:
            l.append([key,count_])
    return l


################# a=  40 08 00 00 04 00 00 00 in L, R format
############### t= 04 00 00 00 left half after K3 is applied  
a=list(np.concatenate(([0,1,0,0],[0]*8,[1,0,0,0],[0]*16,[0]*4,[0,1,0,0],[0]*24)))
#a=list(np.concatenate(([0]*4,[0,1,0,0],[0]*24,[0,1,0,0],[0]*8,[1,0,0,0],[0]*16)))
t=list(np.concatenate(([0]*4,[0,1,0,0],[0]*24)))
p=1/16
#P1=generatePlaintextpairs(a,1000)
#generateFile(P1,"")
P=readfile("C:/Users/ananyae/Downloads/final_input (6).txt")
C=readfile("C:/Users/ananyae/Downloads/final_output (6).txt")
C=makearrCintobits(C)
ans1=seperatealldata(C,[2,5,6,7,8],t,p)
#print(len(ans1[2]["arr"]))
l=spe(ans1[2]["arr"],ans1[2]["count"])
print("S2\n",l)
l=spe(ans1[5]["arr"],ans1[5]["count"])
print("S5\n",l)
l=spe(ans1[6]["arr"],ans1[6]["count"])
print("S6\n",l)
l=spe(ans1[7]["arr"],ans1[7]["count"])
print("S7\n",l)
l=spe(ans1[8]["arr"],ans1[8]["count"])
print("S8\n",l)
#printans(ans1)
################  00 20 00 08 00 00 04 00 
b=np.concatenate(([0]*8,[0,0,1,0],[0]*16,[1,0,0,0],[0]*20,[0,1,0,0],[0]*8))
#b=np.concatenate(([0]*20,[0,1,0,0],[0]*16,[0,0,1,0],[0]*16,[1,0,0,0]))
t_=np.concatenate(([0]*20,[0,1,0,0],[0]*8))
p=1/16
#P2=generatePlaintextpairs(b,1000)
#generateFile(P2,1)
P=readfile("C:/Users/ananyae/Downloads/final_input (7).txt")
C=readfile("C:/Users/ananyae/Downloads/final_output (7).txt")
C=makearrCintobits(C)
ans2=seperatealldata(C,[1,2,4,5,6],t_,p)
print(len(ans2[2]["arr"]))
l=spe(ans2[1]["arr"],ans2[1]["count"])
print("S1\n",l)
l=spe(ans2[4]["arr"],ans2[4]["count"])
print("S4\n",l)

