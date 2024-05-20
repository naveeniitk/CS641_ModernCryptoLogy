import numpy as np 
key56_6=[0,1,1,"x",1,0,0,"x","x",1,1,"x",1,1,1,0,0,"x","x",1,1,"x","x",1,"x","x",0,1,1,1,0,1,0,0,"x",1,1,"x",0,1,1,1,"x",0,0,1,0,0,1,0,1,0,0,"x",0,0]
def rightshift(arr):
    a=arr[0:len(arr)-1]
    ans=list(np.concatenate(([arr[len(arr)-1]],a)))
    return ans
def leftshift(arr):
    a=arr[1:len(arr)]
    ans=list(np.concatenate((a,[arr[0]])))
    return ans
def rightshiftbysomenumber(arr,num):
    ans=arr
    for i in range(num):
        ans=rightshift(ans)
    return ans
def leftshiftbysomenumber(arr,num):
    ans=arr
    for i in range(num):
        ans=leftshift(ans)
    return ans
def PC2(arr):
    per=[14, 17, 11, 24,  1, 5, 3, 28 ,15,  6, 21, 10, 23, 19, 12,  4, 26, 8, 16,  7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    ans=[]
    for i in per:
        ans.append(arr[i-1])
    return ans

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

########################################################
'''key6=List_to_String(PC2(key56_6))
print(key6)
'''
C6=key56_6[0:28]
D6=key56_6[28:]
C0=rightshiftbysomenumber(C6,10)
D0=rightshiftbysomenumber(D6,10)
initialkey=np.concatenate((C0,D0))

print(Converttostring(initialkey))
def generatekeys(bigkey):
    C0=bigkey[0:28]
    D0=bigkey[28:]
    C1=leftshiftbysomenumber(C0,1)
    D1=leftshiftbysomenumber(D0,1)
    in1=list(np.concatenate((C1,D1)))
    key1=PC2(in1)
    C2=leftshiftbysomenumber(C1,1)
    D2=leftshiftbysomenumber(D1,1)
    in2=list(np.concatenate((C2,D2)))
    key2=PC2(in2)
    C3=leftshiftbysomenumber(C2,2)
    D3=leftshiftbysomenumber(D2,2)
    in3=list(np.concatenate((C3,D3)))
    key3=PC2(in3)
    C4=leftshiftbysomenumber(C3,2)
    D4=leftshiftbysomenumber(D3,2)
    in4=list(np.concatenate((C4,D4)))
    key4=PC2(in4)
    C5=leftshiftbysomenumber(C4,2)
    D5=leftshiftbysomenumber(D4,2)
    in5=list(np.concatenate((C5,D5)))
    key5=PC2(in5)
    C6=leftshiftbysomenumber(C5,2)
    D6=leftshiftbysomenumber(D5,2)
    in6=list(np.concatenate((C6,D6)))
    key6=PC2(in6)
    return [key1,key2,key3,key4,key5,key6]

def desoneround(R,L,key):
    ER=Xor(Permutation(ApplySblock(Xor(Expansion(R),key))),L)
    return [ER,R]

def fulldes(P,keys):
    plaintext=IP(Text_to_Bits(P))
    L=plaintext[0:32]
    R=plaintext[32:]
    for i in keys:
        ans=desoneround(R,L,i)
        R=ans[0]
        L=ans[1]
    finalans=list(np.concatenate((L,R)))
    ciphertext=REP(finalans)
    return Bits_to_Text(ciphertext)
    
def substituteininitialkey(initialkey,arr):
    key=[]
    pos=0
    for i in range(len(initialkey)):
        charati=initialkey[i]
        if charati=="x":
            charati=arr[pos]
            pos+=1
        key.append(int(charati))
    return key
def Bruteforce(arr,l):
    if len(arr)==l:
        arr=[int(i) for i in arr]
        bigkey=substituteininitialkey(initialkey,arr)
        keys=generatekeys(bigkey)
        ciphertext=fulldes("hhhhggggffffoooo", keys)
        #actualvalue="qsqmgfikghiushjj"
        actualvalue="kspkroqlgopotlts"
        if actualvalue==ciphertext:
            print(bigkey)
        return 
    t=list(np.concatenate((arr,[int(1)])))
    Bruteforce(t,l)
    t_=list(np.concatenate((arr,[int(0)])))
    Bruteforce(t_,l)

Bruteforce([],14)
bigkeys=[0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1]
print(Converttostring(bigkeys))
##### decrypting for one round #############


def decryptoneround(C,key):
    R1=C[32:]
    L1=C[0:32]
    R0=L1
    L0=Xor(Permutation(ApplySblock(Xor(Expansion(R0),key))),R1)
    return list(np.concatenate((L0,R0)))

def takeoneroundback(C,key):
    ans=decryptoneround(C,key)
    return ans
def decrypt6rounds(C,keys):
    ciphertext=REP_inverse(Text_to_Bits(C))
    for i in range(len(keys)):
        ciphertext=takeoneroundback(ciphertext,keys[len(keys)-1-i])
    plaintext=Bits_to_Text(IP_inverse(ciphertext))
    return plaintext
keys=generatekeys(bigkeys)
ciphertext="ghphikqnkqhjsgshkipfnsoqkpjpggrm "
c1=decrypt6rounds(ciphertext[0:16],keys)
c2=decrypt6rounds(ciphertext[16:],keys)
print(c1,c2,sep="")
ans="ghphikqnkqhjsgshkipfnsoqkpjpggrm"

ans='mhmfmmlslklglomflslgifififififif'
ans=Text_to_Bits(ans)

# rpwmeaipma