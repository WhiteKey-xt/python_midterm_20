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