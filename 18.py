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