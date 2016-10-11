import json
import os
import re
import sys

stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself',
             'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself',
             'they',
             'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those',
             'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
             'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at',
             'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',
             'above',
             'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then',
             'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
             'most',
             'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't',
             'can', 'will', 'just', 'don', 'should', 'now', ]
punctuations = ['!', '"', '#', '$', '%', '&', '\'', ',', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
                '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

dictionary = {}
spamCount = 0
spamFileno = 0
hamCount = 0
hamFileno = 0
uniquewords = set()
initialDict = {}
probabilityDict = {}


def appendfunc():
    for x in range(0, len(content)):
        if content[x] not in stopwords:
            if content[x] in punctuations:
                content[x] = content[x].replace(content[x], " ")
            bagofwords.append(content[x])


def initialList(initialDict):
    global spamCount, hamCount
    if (hamFlag == 1):
        initialDict['ham'] = initialDict['ham'] + 1

    if (spamFlag == 1):
        initialDict['spam'] = initialDict['spam'] + 1

    return initialDict


def assignZero():
    initialDict = {'spam': 0, 'ham': 0}

    return initialDict


def writeJSON(condProb):
    with open('nbmodel.txt', 'w+') as f:
        json.dump(condProb, f)


def calculatep():
    for x in range(0, len(bagofwords)):
        uniquewords.add(bagofwords[x])
        if bagofwords[x] not in dictionary:
            initialDict = assignZero()

        else:
            initialDict = dictionary[bagofwords[x]]
        initialDict = initialList(initialDict)
        dictionary[bagofwords[x]] = initialDict
        # print(initialDict)print the spam and ham count of a word
        # print(dictionary)
        # prints the word along with how many times it occours in spam and ham
        # print(len(uniqueSet))


def probdistribution():
    for key in dictionary:
        finalList = {}
        initialDict = dictionary[key]
        finalList['spam'] = (initialDict['spam'] + 1) / float(spamCount + len(uniquewords))
        finalList['ham'] = (initialDict['ham'] + 1) / float(hamCount + len(uniquewords))
        probabilityDict[key] = finalList
    writeJSON(probabilityDict)


for root, dirs, files in os.walk(sys.argv[1]):
    for i in range(0, len(files)):
        bagofwords = []
        hamFlag = 0
        spamFlag = 0
        if files[i] not in ['README.md', '.DS_Store', 'README.txt', 'LICENSE']:
            filename = root + '/' + files[i]
            # print(filename)
            f = open(filename, 'r', encoding="latin1")
            # print("hello")
            content = f.read()
            content = content.lower()
            
            content = content.split()
            # print contents
            appendfunc()

            # print(bagofwords)
            if (re.search(r'(.)*spam(.)*', root)):
                spamFlag = 1
                spamCount = spamCount + len(bagofwords)
                spamFileno = spamFileno + 1
            elif (re.search(r'(.)*ham(.)*', root)):
                hamFlag = 1
                hamCount = hamCount + len(bagofwords)
                hamFileno = hamFileno + 1
                # print(spamFileno)
                # print(hamFileno)
            calculatep()
probdistribution()
# print(probabilityDict)

# print("done")
