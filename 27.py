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