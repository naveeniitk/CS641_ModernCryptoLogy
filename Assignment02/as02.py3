import numpy as np
k="security"
k=k.lower()
l=len(k)
a="TR XYCB MH AFC MUVY EOHPTCS AFCSS TE QCSI NTYIMS TNA AFCSC EMRBH XAA VAFR MIUCQPUH LMRL_CCETOT FN HM AKUXAHK OTA WANAOTXT FFU EISCWNAF HME BFU MCVA UGTOTRE BM HYLF IFU UVTY ANEHBSEI QYOQM OUVSF AM EAFTE PYHYS XNSKE IFUSC"
# a=list(map(str,input().split()))
a=a.lower()
a=a.replace("j","i")
a=list(a)
an=list()
for i in a:
    if(i!=" " and i!="_"):
        an.append(i)

le=len(an)

if(le%2!=0):
    an.append("z")
    le+=1


b=list()
e=list()
for i in range(97,123):
    if(chr(i)!="j"):
        e.append(chr(i))
m=0
n=0
d={}
for i in range(5):
    c=[]
    while(len(c)!=5):
        if(n!=l and k[n] not in d):
            c.append(k[n])
            d[k[n]]=1
            n+=1
        elif(e[m] not in d):
            c.append(e[m])
            d[e[m]]=1
            m+=1
        else:
            m+=1

    b.append(c)


key=np.array(b)

r=np.where(key=="r")

res=[]

for i in range(0,le,2):
    r1=np.argwhere(key==an[i])
    r2=np.argwhere(key==an[i+1])
    
    if(r1[0][1] == r2[0][1]):
        if(r1[0][0]!=0):
            res.append(key[r1[0][0]-1][r1[0][1]])
        elif(r1[0][0]==0):
            res.append(key[4][r1[0][1]])

        if(r2[0][0]!=0):
            res.append(key[r2[0][0]-1][r2[0][1]])
        elif(r2[0][0]==0):
            res.append(key[4][r2[0][1]])
    elif(r1[0][0]==r2[0][0]):
        if(r1[0][1]!=0):
            res.append(key[r1[0][0]][r1[0][1]-1])
        elif(r1[0][1]==0):
            res.append(key[r1[0][0]][4])
        if(r2[0][1]!=0):
            res.append(key[r2[0][0]][r2[0][1]-1])
        elif(r2[0][1]==0):
            res.append(key[r2[0][0]][4])

    else:
        res.append(key[r1[0][0]][r2[0][1]])
        res.append(key[r2[0][0]][r1[0][1]])

final_string=str()
for i in range(len(res)):
    final_string+=res[i]
print(final_string)
