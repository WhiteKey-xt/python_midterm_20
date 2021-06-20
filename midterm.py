#2-01
n1=int(input("請輸入一個度數（正整數）："))
s1=0
s2=0
if n1<=120:
    s1=120*2.1
    s2=120*2.1
else:
    s1=n1*2.1
    s2=n1*2.1
if 120<n1<=330:
    s1=120*2.1+(n1-120)*3.02
    s2=120*2.1+(n1-120)*2.68
if 330<n1<=500:
    s1=120*2.1+(330-120)*3.02+(n1-330)*4.39
    s2=120*2.1+(330-120)*2.68+(n1-330)*3.61
if 500<n1<=700:
    s1=120*2.1+(330-120)*3.02+(500-330)*4.39+(n1-500)*4.97
    s2=120*2.1+(330-120)*2.68+(500-330)*3.61+(n1-500)*4.01
if n1>700:
    s1=120*2.1+(330-120)*3.02+(500-330)*4.39+(700-500)*4.97+(n1-700)*5.63
    s2=120*2.1+(330-120)*2.68+(500-330)*3.61+(700-500)*4.01+(n1-700)*4.5
print("Summer months:"+str(s1))
print("Non-Summer months:"+str(s2))



#3-02
n2=int(input("請輸入年份："))
s3=n2%12
if s3==0:
    print("monkey")
elif s3==1:
    print("rooster")
elif s3==2:
    print("dog")
elif s3==3:
    print("pig")
elif s3==4:
    print("rat")
elif s3==5:
    print("ox")
elif s3==6:
    print("tiger")
elif s3==7:
    print("rabbit")
elif s3==8:
    print("dragon")
elif s3==9:
    print("snake")
elif s3==10:
    print("horse")
elif s3==11:
    print("sheep")


#4-03
n3=int(input("請輸入X值："))
n4=int(input("請輸入Y值："))
s4=n3**2+n4**2
if n3==0 and n4==0:
    print("該點位於原點。")
elif n3>0 and n4>0:
    print("該點位於第一象限，離原點距離為根號"+str(s4)+"。")
elif n3<0 and n4<0:
    print("該點位於第三象限，離原點距離為根號"+str(s4)+"。")
elif n3>0 and n4<0:
    print("該點位於第二象限，離原點距離為根號"+str(s4)+"。")
elif n3<0 and n4>0:
    print("該點位於第四象限，離原點距離為根號"+str(s4)+"。")
elif n3==0 and n4>0:
    print("該點位於上半平面Y軸，離原點距離為根號"+str(s4)+"。")
elif n3>0 and n4==0:
    print("該點位於右半平面X軸，離原點距離為根號"+str(s4)+"。")
elif n3==0 and n4<0:
    print("該點位於下半平面Y軸，離原點距離為根號"+str(s4)+"。")
elif n3<0 and n4==0:
    print("該點位於左半平面X軸，離原點距離為根號"+str(s4)+"。")


#5-04
n5=int(input("請輸入階層值："))
s5=1
s6=0
while (s5<=n5):
    s6+=1
    s5*=s6
print(s6)


#9-05
n6=input("輸入s1為：")
n7=input("輸入s2為：")
if n6 in n7:
    print("YES")
else:
    print("NO")


#13-06
n8=input("輸入一字元為：")
if n8==n8[::-1]:
   print("YES")
else:
    print("NO")


#14-07
n9=input("輸入一字串為：")
print("There are "+str(n9.count("")-1)+" characters")


#15-08
n10=input("輸入一組四位數字為：")
s7=list(map(int,n10))
t1=((s7[0]+7)%10)
t2=((s7[1]+7)%10)
t3=((s7[2]+7)%10)
t4=((s7[3]+7)%10)
print(t3,t4,t1,t2)


#17-09
n11=input("")
o1=n11.replace("A","1")
o2=o1.replace("J","11")
o3=o2.replace("Q","12")
o4=o3.replace("K","13")
o5=o4.split(" ")
o6=int(o5[0])+int(o5[1])+int(o5[2])+int(o5[3])+int(o5[4])
print(str(o6))


#18-10
n12=int(input("測試的資料量:"))
s9=[]
for i in range(1,n12+1):
    p1=input().split(" ")
    if p1[0]=="O" and p1[1]=="O" and p1[2]=="O":
        s9.append("YES")
    elif p1[0]=="O" and p1[1]=="A" and(p1[2]=="O" or p1[2]=="A"):
        s9.append("YES")
    elif p1[0]=="O" and p1[1]=="B" and(p1[2]=="O" or p1[2]=="B"):
        s9.append("YES")
    elif p1[0]=="O" and p1[1]=="AB" and(p1[2]=="A" or p1[2]=="B"):
        s9.append("YES")
    elif p1[0]=="A" and p1[1]=="A" and(p1[2]=="O" or p1[2]=="A"):
        s9.append("YES")
    elif p1[0]=="B" and p1[1]=="A" and(p1[2]=="O" or p1[2]=="A" or p1[2]=="B" or p1[2]=="AB"):
        s9.append("YES")
    elif p1[0]=="A" and p1[1]=="AB" and(p1[2]=="B" or p1[2]=="A" or p1[2]=="AB"):
        s9.append("YES")
    elif p1[0]=="B" and p1[1]=="B" and(p1[2]=="B" or p1[2]=="O"):
        s9.append("YES")
    elif p1[0]=="B" and p1[1]=="AB" and(p1[2]=="B" or p1[2]=="A" or p1[2]=="AB"):
        s9.append("YES")
    elif p1[0]=="AB" and p1[1]=="AB" and(p1[2]=="B" or p1[2]=="A" or p1[2]=="AB"):
        s9.append("YES")                                     
    else:
        s9.append("IMPOSSIBLE")
print(s9)


#19-11
n13=int(input("組數為："))
s10=0
t5=[]
for i in range(1,n13+1):
    s10=0
    x,y=input("第"+str(i)+"組:").split(" ")
    s10+=int(x)*250+int(y)*175
    t5.append(s10)
for j in range (1,n13+1):
    print("第"+str(j)+"組應收費用:"+str(t5[j-1]),end="\n")


#20-12
s11=[["123","Tom","DTGD"],["456","Cat","CSIE"],
    ["789","Nana","ASIE"],["321","Lim","DBA"],["654","Won","FDD"]]
n15=input("輸入查詢學號為：")
if n15=="123":
    print("學生資料為："+str(s11[0]))
elif n15=="456":
    print("學生資料為："+str(s11[1]))
elif n15=="789":
    print("學生資料為："+str(s11[2]))
elif n15=="321":
    print("學生資料為："+str(s11[3]))
elif n15=="654":
    print("學生資料為："+str(s11[4]))
else:
    print("查無此筆資料")


#21-13
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


#25-14
n17=input("檢測的字串（end結束）：")
if n17== "end":
    print("檢測結束")
else:
    t6=input("檢測的單一字元：")
    t7=n17.count(t6)
    print("字元"+t6+"出現次數為："+str(t7))


#27-15
n18=list(input("甲方的數字："))
n19=list(input("乙方的數字："))
s13=""
for i in range(0,len(n18)):
    if n18[i]>n19[i]:
        t8="贏"
        s13+=t8
    elif n18[i]<n19[i]:
        t9="輸"
        s13+=t9
    elif n18[i]==n19[i]:
        t10="和"
        s13+=t10
print("洗刷刷結果："+s13)


#31-16
n20=float(input("國文："))
n21=float(input("英文："))
n22=float(input("微積分："))
n23=float(input("體育："))
n24=float(input("程式設計："))
t11=float((n20+n21+n22+n23+n24)/5)
print("平均分數：%2.2f" % (t11))
t12=dict(n20="國文",n21="英文",n22="微積分",n23="體育",n24="程式設計")
t13=max(n20,n21,n22,n23,n24)
t14=min(n20,n21,n22,n23,n24)
print("最高分科目：程式設計"+str(int(t13))+"分")
print("最低分科目：微積分"+str(int(t14))+"分")


#38-17
n14=int(input(""))
for i in range(0,n14-4):
    for j in range((n14-4)-i):
        print(" ",end="")
    for k in range(2*i+1):
        print("＊",end="")
    print()
    
for i in range(0,(n14-4)+1):
    for j in range(0,i):
        print(" ",end="")
    for k in range(2*(n14-4)+1-2*i):
        print("＊",end="")
    print()


#42-18
n25=input("")
u2=n25.split(" ")
t15=int(u2[0])*int(u2[1])
t16=int(u2[1])-1
print(str(t15)+"x**"+str(t16))


#48-19
n26=input("請輸入英文句子：")
u3=n26.split(" ")
print("輸出結果："+str(u3[::-1]))


#51-20
n27=set("春眠不覺曉處處聞啼鳥夜來風雨聲花落知多少")
n28=set("紅豆生南國春來發幾枝願君多采擷此物最相思")
print(n27&n28)