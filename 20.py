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