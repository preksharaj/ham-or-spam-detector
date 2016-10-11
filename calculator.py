import re
import os

precision = [0]*2
recall = [0]*2
f1 = [0]*2
tp = {'spam':0,'ham':0}
fp = {'spam':0,'ham':0}
fn = {'spam':0,'ham':0}
def calculating():
    precision[0] = tp['spam'] / (tp['spam'] + fp['spam'])
    recall[0] = tp['spam'] / (tp['spam'] + fn['spam'])
    f1[0] = (2 * precision[0] * recall[0]) / (precision[0] + recall[0])
    precision[1] = tp['ham'] / (tp['ham'] + fp['ham'])
    recall[1] = tp['ham'] / (tp['ham'] + fn['ham'])
    f1[1] = (2 * precision[1] * recall[1]) / (precision[1] + recall[1])
        # P = tp/(tp + fp)
def printing():
    print("Precision", "Recal", "f1")
    print("SPAM", round(precision[0], 2), round(recall[0], 2), round(f1[0], 2))
    print("HAM", round(precision[1], 2), round(recall[1], 2), round(f1[1], 2))
    print("F1 avg:", round((sum(f1) / 2.0), 3))

with open('nboutput.txt','r') as outputFile:
    data = outputFile.readlines()

for line in data:
    line = line.strip('\n').split(' ')
        #print(line)
    if (line[0] == 'SPAM') and (re.search(r'(.)*spam(.)*', line[1])):
        tp['spam'] = tp['spam']+1
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
print (tp)
print (fp)
print (fn)
calculating()
        # R = tp/(tp + fn)
printing()
