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