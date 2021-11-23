import urllib.request
from calc import add,subtract,divide,multi


f = open("step_3.txt", "r")
file = f.readlines()
currentline = 0
while currentline <= len(file) - 1:
    line = file[int(currentline)]
    output = line.replace('\n','')
    split = output.split(" ")
    print(split)
    if len(split) == 2:
        currentline = int(split[1]) - 1
    else:
        if split[2] == "+":
           currentline = add(int(split[3]),int(split[4])) - 1
        elif split[2] == "-":
            currentline = subtract(int(split[3]),int(split[4])) - 1
        elif split[2] == "/":
            currentline = divide(int(split[3]),int(split[4])) - 1
        elif split[2] == "x":
            currentline = multi(int(split[3]),int(split[4])) - 1
        else:
            print("not valid operator")