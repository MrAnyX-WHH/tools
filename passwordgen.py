import os
import time
text=("""                            


                        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::            
                        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                        :::::important note:this is generator created by Mr.AnyX:::
                        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                            




""")
for i in text:
    print(i,end="",flush=True)
    time.sleep(0.01)







def fourth():
    x1=input("[+]character1:==> ")
    x2=input("[+]character2:==> ")
    x3=input("[+]character3:==> ")
    x4=input("[+]character4:==> ")
    data=[x1+x1,x1+x2,x1+x3,x1+x4,x2+x1,x2+x2,x2+x3,x2+x4,x3+x1,x3+x2,x3+x3,x3+x4,x1+x1+x1,
    x1+x1+x2,x1+x1+x3,x1+x1+x4,x1+x2+x1,x1+x2+x2,x1+x2+x3,x1+x2+x4,x1+x3+x1,
    x1+x3+x2,x1+x3+x3,x1+x3+x4,x2+x1+x1,
    x2+x1+x2,x2+x1+x3,x2+x1+x4,x2+x2+x1,x2+x2+x2,x2+x2+x3,x2+x2+x4,x2+x3+x1,
    x2+x3+x2,x2+x3+x3,x2+x3+x4,x3+x1+x1,
    x3+x1+x2,x3+x1+x3,x3+x1+x4,x3+x2+x1,x3+x2+x2,x3+x2+x3,x3+x2+x4,x3+x3+x1,
    x3+x3+x2,x3+x3+x3,x3+x3+x4,x3+x4+x1,x3+x4+x2,x3+x4+x3,x3+x4+x4,x4+x4+x1,x4+x4+x2,x4+x4+x3,x4+x4+x4,
    x1+x1+x1+x1,
    x1+x1+x1+x2,x1+x1+x1+x3,x1+x1+x1+x4,x1+x1+x2+x1,x1+x1+x2+x2,x1+x1+x2+x3,x1+x1+x2+x4,x1+x1+x3+x1,
    x1+x1+x3+x2,x1+x1+x3+x3,x1+x1+x3+x4,x1+x2+x1+x1,
    x1+x2+x1+x2,x1+x2+x1+x3,x1+x2+x1+x4,x1+x2+x2+x1,x1+x2+x2+x2,x1+x2+x2+x3,x1+x2+x2+x4,x1+x2+x3+x1,
    x1+x2+x3+x2,x1+x2+x3+x3,x1+x2+x3+x4,x1+x3+x1+x1,
    x1+x3+x1+x2,x1+x3+x1+x3,x1+x3+x1+x4,x1+x3+x2+x1,x1+x3+x2+x2,x1+x3+x2+x3,x1+x3+x2+x4,x1+x3+x3+x1,
    x1+x3+x3+x2,x1+x3+x3+x3,x1+x3+x3+x4,x1+x3+x4+x1,x1+x3+x4+x2,x1+x3+x4+x3,x1+x3+x4+x4,x1+x4+x1+x1,
    x1+x4+x1+x2,x1+x4+x1+x3,x1+x4+x1+x4,x1+x4+x2+x1,x1+x4+x2+x2,x1+x4+x2+x3,x1+x4+x2+x4,x1+x4+x3+x1,
    x1+x4+x3+x2,x1+x4+x3+x3,x1+x3+x4+x4,x1+x4+x4+x1,x1+x4+x4+x2,x1+x4+x4+x3,x1+x4+x4+x4,x2+x1+x1+x1,
    x2+x1+x1+x2,x2+x1+x1+x3,x2+x1+x1+x4,x2+x1+x2+x1,x2+x1+x2+x2,x2+x1+x2+x3,x2+x1+x2+x4,x2+x1+x3+x1,
    x2+x1+x3+x2,x2+x1+x3+x3,x2+x1+x3+x4,x2+x2+x1+x1,
    x2+x2+x1+x2,x2+x2+x1+x3,x2+x2+x1+x4,x2+x2+x2+x1,x2+x2+x2+x2,x2+x2+x2+x3,x2+x2+x2+x4,x2+x2+x3+x1,
    x2+x2+x3+x2,x2+x2+x3+x3,x2+x2+x3+x4,x2+x3+x1+x1,
    x2+x3+x1+x2,x2+x3+x1+x3,x2+x3+x1+x4,x2+x3+x2+x1,x2+x3+x2+x2,x2+x3+x2+x3,x2+x3+x2+x4,x2+x3+x3+x1,
    x2+x3+x3+x2,x2+x3+x3+x3,x2+x3+x3+x4,x2+x3+x4+x1,x2+x3+x4+x2,x2+x3+x4+x3,x2+x3+x4+x4,x2+x4+x1+x1,
    x2+x4+x1+x2,x2+x4+x1+x3,x2+x4+x1+x4,x2+x4+x2+x1,x2+x4+x2+x2,x2+x4+x2+x3,x2+x4+x2+x4,x2+x4+x3+x1,
    x2+x4+x3+x2,x2+x4+x3+x3,x2+x3+x4+x4,x2+x4+x4+x1,x2+x4+x4+x2,x2+x4+x4+x3,x2+x4+x4+x4,x3+x1+x1+x1,
    x3+x1+x1+x2,x3+x1+x1+x3,x3+x1+x1+x4,x3+x1+x2+x1,x3+x1+x2+x2,x3+x1+x2+x3,x3+x1+x2+x4,x3+x1+x3+x1,
    x3+x1+x3+x2,x3+x1+x3+x3,x3+x1+x3+x4,x3+x2+x1+x1,
    x3+x2+x1+x2,x3+x2+x1+x3,x3+x2+x1+x4,x3+x2+x2+x1,x3+x2+x2+x2,x3+x2+x2+x3,x3+x2+x2+x4,x3+x2+x3+x1,
    x3+x2+x3+x2,x3+x2+x3+x3,x3+x2+x3+x4,x3+x3+x1+x1,
    x3+x3+x1+x2,x3+x3+x1+x3,x3+x3+x1+x4,x3+x3+x2+x1,x3+x3+x2+x2,x3+x3+x2+x3,x4+x3+x2+x4,x3+x3+x3+x1,
    x3+x3+x3+x2,x3+x3+x3+x3,x3+x3+x3+x4,x3+x3+x4+x1,x3+x3+x4+x2,x3+x3+x4+x3,x3+x3+x4+x4,x3+x4+x1+x1,
    x3+x4+x1+x2,x3+x4+x1+x3,x3+x4+x1+x4,x3+x4+x2+x1,x3+x4+x2+x2,x3+x4+x2+x3,x3+x4+x2+x4,x3+x4+x3+x1,
    x3+x4+x3+x2,x3+x4+x3+x3,x3+x3+x4+x4,x3+x4+x4+x1,x3+x4+x4+x2,x3+x4+x4+x3,x3+x4+x4+x4,x4+x1+x1+x1,
    x4+x1+x1+x2,x4+x1+x1+x3,x4+x1+x1+x4,x4+x1+x2+x1,x4+x1+x2+x2,x4+x1+x2+x3,x4+x1+x2+x4,x4+x1+x3+x1,
    x4+x1+x3+x2,x4+x1+x3+x3,x4+x1+x3+x4,x4+x2+x1+x1,
    x4+x2+x1+x2,x4+x2+x1+x3,x4+x2+x1+x4,x4+x2+x2+x1,x4+x2+x2+x2,x4+x2+x2+x3,x4+x2+x2+x4,x4+x2+x3+x1,
    x4+x2+x3+x2,x4+x2+x3+x3,x4+x2+x3+x4,x4+x3+x1+x1,
    x4+x3+x1+x2,x4+x3+x1+x3,x4+x3+x1+x4,x4+x3+x2+x1,x4+x3+x2+x2,x4+x3+x2+x3,x4+x3+x2+x4,x4+x3+x3+x1,
    x4+x3+x3+x2,x4+x3+x3+x3,x4+x3+x3+x4,x4+x3+x4+x1,x4+x3+x4+x2,x4+x3+x4+x3,x4+x3+x4+x4,x4+x4+x1+x1,
    x4+x4+x1+x2,x4+x4+x1+x3,x4+x4+x1+x4,x4+x4+x2+x1,x4+x4+x2+x2,x4+x4+x2+x3,x4+x4+x2+x4,x4+x4+x3+x1,
    x4+x4+x3+x2,x4+x4+x3+x3,x4+x3+x4+x4,x4+x4+x4+x1,x4+x4+x4+x2,x4+x4+x4+x3,x4+x4+x4+x4]
    for i in data:
        file=open(file="passw.txt",mode="a")
        file.write(i)
        file.write("\n")
fourth()
