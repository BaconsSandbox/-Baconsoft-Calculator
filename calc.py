print("Welcome To The [BaconSoft] Calculator!")
print("Made by [Baconsoft]2021")
print("Made USING #love in Python 3.10")
print("What is your name?")
name = input("My name is: ")
space = (" ")
ioq = ("Thanks, ")
ioqq = ("!\n")
ioqqq = ("Alright, ")
ioo = ("Ok, ")
io = ("Enter The First Number Of Your Math Problem!")
iuy = ("Enter The Second Number Of Your Math Problem!")
ioj = ("Enter your operation!\n [1] for addition\n [2] for subtraction\n [3] for mutiliplacation\n [4] for division\n")
print(ioo + name + space + io)
i = int(input())
print(ioq + name + ioqq + ioqqq + name + space + iuy)
ii = int(input())
print(ioq + name + ioqq + ioqqq + name + space + ioj)
o = int(input())
if o == 4 and ii == 0:
    print("Syntax Error 9001 (Divide by 0)")
elif o == 1:
    a = int(i + ii)
elif o == 2:
    a = int(i - ii)
elif o == 3:
    a = int(i * ii)
elif o == 4:
    a = int(i / ii)
else:
    print("Syntax Error: 1000 (wrong Opperation)")
    a = ("There was a error in the problem input")
print("The Answer is: ")
print("______________\n")
print(a)
print("Thanks for using The [Baconsoft] Calculator")
quit
