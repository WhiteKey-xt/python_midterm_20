n17=input("檢測的字串（end結束）：")
if n17== "end":
    print("檢測結束")
else:
    t6=input("檢測的單一字元：")
    t7=n17.count(t6)
    print("字元"+t6+"出現次數為："+str(t7))