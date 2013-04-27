#! /usr/bin/python
# Author : Camille Mougey
# See http://blog.4j4x.net/ for more information
import subprocess, random, argparse
import re

argparser = argparse.ArgumentParser()
argparser.add_argument("level", help = "Password level, between 100 and 400", type=int)
argparser.add_argument("john", help = "JohnTheRipper path (/somepath/run/)")
argparser.add_argument("-r", "--gen-data", help = "Generate the data file", action = "store_true")
argparser.add_argument("-m", "--max-len", help = "Maximum length for password", type = int,
                       default = 12)
args = argparser.parse_args()


lvl = args.level
john_path = args.john
max_len = args.max_len

# Re-gen data if asked
if (args.gen_data):
    genmkvpwd = subprocess.Popen([john_path + "genmkvpwd",
                                  john_path + "stats",
                                  "0",
                                  str(max_len)],
                                 stdout = subprocess.PIPE)
    info = genmkvpwd.communicate()[0]
    file = open("data", "w")
    file.write(info)
    file.close()

# Parsing data
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

# Compute password
deb = random.randint(0, int(data[str(lvl)]))
john = subprocess.Popen([john_path + "john",
                         "-markov=%s:%s:%s:%s" % (lvl, deb, deb, max_len),
                         "--stdout"], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
res = john.communicate()[0]
print res.split("\n")[-2]
