import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
symbols="[]{}()*/-+:;_"
a=lower+upper+number+symbols

print(f"{lower}\n{upper}\n{number}\n{symbols}\n"
      "tepadagi belgilardan parol tuzing!!!")
kod=input(">>>")
length=len(kod)
if len(kod)==length:
    while True:
        passwoard="".join(random.sample(a,length))
        if passwoard==kod:
            print(f"parol: {passwoard}")
            break
else:
    print("kiritgan kod 4 talik emas!!!")
