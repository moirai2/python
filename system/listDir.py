#!/usr/bin/python
import os
import glob
import sys
import optparse
import re
############################## options ##############################
parser=optparse.OptionParser()
parser.add_option('-g',action="store",help="filename to grep",dest="grep")
parser.add_option('-G',action="store",help="filename to ungrep",dest="ungrep")
parser.add_option('-r',action="store",help="recursive search",dest="recursive",type="int",default=0)
(options,args)=parser.parse_args()
if options.grep!=None:options.grep=re.compile(options.grep)
if options.ungrep!=None:options.ungrep=re.compile(options.ungrep)
############################## listDir ##############################
def listDir(path=".",recursion=0,grep=None,ungrep=None):
    array=[]
    files=os.listdir(path)
    for f in files:
        if path==".":file=f
        else:file=path+"/"+f
        if f.startswith("."):continue
        if os.path.isdir(file):
            if recursion==0:continue
            array.extend(listDir(file,recursion-1,grep,ungrep))
        if grep!=None:
            if not grep.search(f):continue
        if ungrep!=None:
            if ungrep.match(f):continue
        array.append(file)
    return array
############################## printLines ##############################
def printLines(list):
    for l in list:print(l)
############################## main ##############################
if len(args)<1:
    print("python listDir.py DIR/FILE > LIST",file=sys.stderr)
    sys.exit(1)
for path in args:
    printLines(listDir(path,options.recursive,options.grep,options.ungrep))