import urllib.request
from calc import add,subtract,divide,multi


url = "https://gist.githubusercontent.com/Jonesey13/47029d880ab17a2df41df7a677fb4e89/raw/78e0e3516d46dbe10cfae147bc2e270b7e8cc2c0/step_2.txt"
file = urllib.request.urlopen(url)

for line in file:
    output = line.decode('utf-8')
    output = output.replace('\n','')
    split = output.split(" ")
    if split[1] == "+":
        print(add(int(split[2]),int(split[3])))
    elif split[1] == "-":
        print(subtract(int(split[2]),int(split[3])))
    elif split[1] == "/":
        print(divide(int(split[2]),int(split[3])))
    elif split[1] == "x":
        print(multi(int(split[2]),int(split[3])))
    else:
        print("not valid operator")