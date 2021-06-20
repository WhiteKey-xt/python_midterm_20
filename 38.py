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