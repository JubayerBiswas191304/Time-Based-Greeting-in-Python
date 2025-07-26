import time

GTime=int(time.strftime("%H"))

print("Now time is",time.strftime("%H:%M:%S"))


time=GTime

if(time<=5 or time>=20):
    print("Good Night!")

elif(time>=18):
    print("Good evening!")

elif(time>=12):
    print("Good afternoon!")
else:
    print("Good Morning!")