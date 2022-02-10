#yil-asr
yil=int(input("yilni kiriting: "))
a=yil//100
b=yil%100

if b>0:
    c=a+1
    print(c,"-asr")
else:
    print(a,"-asr")



