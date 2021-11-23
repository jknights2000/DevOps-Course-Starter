import urllib.request
from calc import add,subtract,divide,multi


f = open("step_3.txt", "r")
file = f.readlines()
numbers = []
calcs = []
currentline = 0
while currentline <= len(file) - 1:
    line = file[int(currentline)]
    output = line.replace('\n','')
    split = output.split(" ")
    print(currentline)
    if len(split) == 2:
        if int(split[1]) in numbers:
            break
        else:
            currentline = int(split[1]) - 1
            numbers.append(int(split[1]))
    else:
        
        leave = False
        newdict = {"op":split[2],"n1":split[3],"n2":split[3]}
        for dict in calcs:
            if dict["op"] == newdict["op"] and dict["n2"] == newdict["n2"] and dict["n1"] == newdict["n1"]:
                leave = True
        if leave:
            break

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