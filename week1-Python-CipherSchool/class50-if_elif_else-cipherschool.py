age=int(input("enter your age"))
if 0<age<=3:
    print("ticket is free")
elif 4<age<=10:
    print("price is 150")
elif 11<age<=60:
    print("price is 250")
else:
    print("price is 200")