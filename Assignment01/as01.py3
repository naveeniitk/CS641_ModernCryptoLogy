def replac_(a,dic):
    ans=''
    for i in range(0,len(a)):
        j=a[i]
        if j in dic.keys():
            ans=ans+dic[j]
        else:
            ans=ans+j
    return ans
a=" wsam ie pjo ysgtm eyipbya .P axg niphay y,mey syw ahgm ewhrg tw hmysyam wh meyiepjoys .Ag jygtmeyk pmys ie pjo ysavw kkoyjgsywhmy sy amwh rmephmewagh y!Me yigu ynay utgsmew ajya apr ywap awjfkya no a mwmnmwghiwfeyswhve wieuwr wm aepby oyyhae wtmyuox8 fkpiya. Me y fpaavgs uwa mxSrN03u wddvwmegnmmey dngmya. Mew awameyt".lower()
c=0
d=dict()
for j in range(0,len(a)):
    i=a[j]
    c=c+1
    if i not in d.keys():
        d[i]=0
    d[i]=d[i]+1
for j in d.keys():
    if j !=" ":
        d[j]=round(d[j]*100/(c-16),1);
print(d)
print()
print()
dnew={"y":"e","m":"t","e":"h","w":"i","a":"s","f":"p","p":"a","v":"w","g":"o","s":"r","u":"d","n":"u","d":"q","i":"c","h":"n","k":"l","j":"m","o":"b","t":"f","b":"v","x":"y","r":"g"}
print(len(dnew.keys()))
#dnew={"y":"a","a":"i"}
#dnew={"w":"t","s":"h","a":"i","m":"s"}
print(a)
print()
print()
print(replac_(a, dnew))
