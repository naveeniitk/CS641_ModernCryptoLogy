def M(a,b,mod):
    res=1
    while(b>0):
        if(b%2==1):
            res=(res*a)%mod 
        a=((a%mod) *(a%mod))
        b=b//2
    return res

def I(a,mod):
    return M(a, mod-2, mod)


# print(I(324,19807040628566084398385987581))
ans = 324*I(324,19807040628566084398385987581)
# print(ans//19807040628566084398385987581 , ans%19807040628566084398385987581)


mod=19807040628566084398385987581
print()


# 11226815350263531814963336315
g9189=4138652629655613570819000497*I(11226815350263531814963336315,19807040628566084398385987581)
print("g9189       : ",g9189%mod)
print()


g2021=I(11226815350263531814963336315, mod)*9190548667900274300830391220
print("g2021       : ",g2021%mod)
print()

g2021_4_num = ((I(((g2021)**4),mod)) * (g9189))%mod
# print("g2021_4_num : ",g2021_4_num%mod)
# print()

g1105=g2021_4_num
print("g1105       : ",g1105%mod)
print()

g916= (g2021*(I(g1105,mod)))%mod
print("g916        : ",g916%mod)
print()


g189 = ((g1105)*(I(g916,mod)))%mod
print("g189        : ",g189)
print()


g160= (I((g189**4),mod) * g916 )%mod
print("g160        : ",g160%mod)
print()


g29= (I(g160, mod) * g189 )%mod
print("g29         : ",g29%mod)
print()


g15 = (I(g29**5, mod)*g160) %mod
print("g15         : ",g15%mod)
print()


g14 = (I(g15, mod)*g29) %mod
print("g14         : ",g14%mod)
print()


g1 = (I(g14, mod)*g15) % mod
print( "g1          : ",g1%mod)
print()

inverse_g = I(g1, mod)
print("g : " ,inverse_g)
print()

# password =11226815350263531814963336315//(I(g1**324,mod))

tmp= inverse_g


for i in range(1,324):    
    inverse_g = (inverse_g * tmp) % mod

password = (inverse_g * 11226815350263531814963336315 )% mod


print("password   : ",password)




# enter - enter - pluck -climb - give - (take magic words ) - back - back - (magic word ) - read - pasword ( 3608528850368400786036725)

# (324, 11226815350263531814963336315)
# (2345,9190548667900274300830391220)
# (9513, 4138652629655613570819000497)
