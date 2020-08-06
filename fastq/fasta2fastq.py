#!/usr/bin/python
import os
import sys
import tempfile
import shutil
import optparse
############################## options ##############################
parser=optparse.OptionParser()
parser.add_option('-o',action="store",help="output file",dest="output",default="-")
(options,args)=parser.parse_args()
############################## fasta2fastq ##############################
def fasta2fastq(reader,writer):
    while True:
        idLine=reader.readline()
        if not idLine:return
        seqLine=reader.readline()
        idLine=idLine[1:].strip()
        seqLine=seqLine.strip()
        length=len(seqLine)
        qualLine=""
        for i in range(length):qualLine+="/"
        writer.write("@"+idLine+"\n")
        writer.write(seqLine+"\n")
        writer.write("+"+"\n")
        writer.write(qualLine+"\n")
############################## main ##############################
temp=None
if len(args)==0:args.append("-")
if options.output=='-':writer=sys.stdout
else:
    (fp,temp)=tempfile.mkstemp(prefix='temp')
    writer=open(temp,'w+t')
for file in args:
    if file=='-':reader=sys.stdin
    else:reader=open(file)
    fasta2fastq(reader,writer)
writer.close()
if options.output!='-':
    shutil.move(temp,options.output)
    os.chmod(options.output,0o755)