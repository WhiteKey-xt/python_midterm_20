s12=[[123,456,9000],[456,789,5000],[789,888,6000],[336,558,10000],[775,666,12000],[566,221,7000]]
n16=int(input("輸入查詢組數N為:"))
user=[]
s13=""
for i in range(n16):
    u1=input()
    user=u1.split(" ")
    if(int(user[0])==s12[i][0]):
        if(int(user[1])==s12[i][1]):
            ans+=str(s12[i][2])+"\n"
    else:
        ans+="error\n"
print(s13)