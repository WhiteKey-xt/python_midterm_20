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