import re

data = {}

fi = open("data", "r")
for l in fi.readlines():
    lvl = re.findall("lvl=([0-9]*)", l)[0]
    count = re.findall("passwords \(([0-9]*)\)", l)
    if (len(count) < 1):
       count = re.findall("([0-9])* possible", l)[0]
    else :
       count = count[0]
    data[lvl] = count

