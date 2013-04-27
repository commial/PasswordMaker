#! /usr/bin/python

import subprocess, random, argparse
from parse import *

argparser = argparse.ArgumentParser()
argparser.add_argument("level", help = "Password level, between 100 and 400", type=int)
argparser.add_argument("john", help = "JohnTheRipper path (/somepath/run/)")
args = argparser.parse_args()

lvl = args.level
deb = random.randint(0, int(data[str(lvl)]))
john_path = args.john

john = subprocess.Popen([john_path + "john",
                         "-markov=" + str(lvl) + ":" + str(deb) + ":" + str(deb) + ":12",
                         "--stdout"], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
res = john.communicate()[0]
print res.split("\n")[-2]
