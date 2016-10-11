import json
import os
import math
import sys

f=open('nboutput.txt', 'w+')
with open('nbmodel.txt', 'r') as data:
    input =json.load(data)



def assignprob():
    #check the higer prob assign that to the msg
    with open('nboutput.txt', 'a+') as writer:
     if (max(hamprob, spamprob) == hamprob):
        writer.write("HAM ")
     else:
        writer.write("SPAM ")
     writer.write(filename+"\n")

def appendfunc():
    for x in range(0, len(contents)):
        bagofwords.append(contents[x])



for root, dirs, files in os.walk(sys.argv[1]):
    for i in range(0, len(files)):
        spamprob = -2
        hamprob = -2
        bagofwords = []
        # print math.log(0.25,2)

        if files[i] not in ['README.md','.DS_Store' ,'README.txt' ,'LICENSE']:
            filename = root + '/' + files[i]
            #print(filename)
            f = open(filename, 'r', encoding="latin1")
            # print("hello")
            contents =f.read()
            contents =contents.lower()
            contents =contents.split()
            #append to bagofwords
            appendfunc()
            #prob caluculate
            for x in range(0, len(bagofwords)):
                if bagofwords[x] in input:

                    spamprob =spamprob +math.log(input[bagofwords[x]]['spam'],2)

                    hamprob =hamprob +math.log(input[bagofwords[x]]['ham'],2)
            #print prob to console
            #print(spamprob, hamprob)
            # print math.pow(2,spamprob),math.pow(2,hamprob)
            assignprob()
f.close()