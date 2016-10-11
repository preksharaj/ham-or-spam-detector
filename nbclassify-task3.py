import json
import os
import math
import sys
import re

stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself',
            'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they',
            'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those',
            'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
            'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at',
            'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above',
            'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then',
            'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most',
            'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't',
            'can', 'will', 'just', 'don', 'should', 'now', ]
punctuations = ['!', '"', '#', '$', '%', '&', '\'', ',', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
                '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

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
        if contents[x] not in stopwords and punctuations:
            bagofwords.append(contents[x])

def check():
    precision = [0] * 2
    recall = [0] * 2
    f1 = [0] * 2
    tp = {'spam': 0, 'ham': 0}
    fp = {'spam': 0, 'ham': 0}
    fn = {'spam': 0, 'ham': 0}

    def calculating():
        precision[0] = tp['spam'] / (tp['spam'] + fp['spam'])
        recall[0] = tp['spam'] / (tp['spam'] + fn['spam'])
        f1[0] = (2 * precision[0] * recall[0]) / (precision[0] + recall[0])
        precision[1] = tp['ham'] / (tp['ham'] + fp['ham'])
        recall[1] = tp['ham'] / (tp['ham'] + fn['ham'])
        f1[1] = (2 * precision[1] * recall[1]) / (precision[1] + recall[1])

    def printing():
        print("Precision", "Recal", "f1")
        print("SPAM", round(precision[0], 2), round(recall[0], 2), round(f1[0], 2))
        print("HAM", round(precision[1], 2), round(recall[1], 2), round(f1[1], 2))
        print("F1 avg:", round((sum(f1) / 2.0), 2))

    with open('nboutput.txt', 'r') as outputFile:
        data = outputFile.readlines()

    for line in data:
        line = line.strip('\n').split(' ')
        # print(line)
        if (line[0] == 'SPAM') and (re.search(r'(.)*spam(.)*', line[1])):
            tp['spam'] += 1
        elif (line[0] == 'SPAM') and (re.search(r'(.)*ham(.)*', line[1])):
            fp['spam'] += 1
        elif (line[0] == 'HAM') and (re.search(r'(.)*spam(.)*', line[1])):
            fn['spam'] += 1

        if (line[0] == 'HAM') and (re.search(r'(.)*ham(.)*', line[1])):
            tp['ham'] += 1
        elif (line[0] == 'HAM') and (re.search(r'(.)*spam(.)*', line[1])):
            fp['ham'] += 1
        elif (line[0] == 'SPAM') and (re.search(r'(.)*ham(.)*', line[1])):
            fn['ham'] += 1
    # print (tp)
    # print (fp)
    # print (fn)
    calculating()
    # R = tp/(tp + fn)
    printing()



for root, dirs, files in os.walk(sys.argv[1]):
    for i in range(0, len(files)):
        spamprob = -2
        hamprob = -2
        bagofwords = []
        # print math.log(0.25,2)

        if files[i] not in ['README.md','.DS_Store' ,'README.txt' ,'LICENSE']:
            filename = root + '/' + files[i]
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

check()


f.close()




