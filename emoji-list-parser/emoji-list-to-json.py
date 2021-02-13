import json

def parseEmoji(line):
    code, comment = line.split(";")
    code = code.strip()
    fullname = comment.split("#")[-1]
    name = ' '.join(fullname.split()[2:])
    return {"code":code, "name":name}


emojiDict = {}

counter = {
'comments' : 0,
'groups' : 0,
'subgroups' : 0,
'emojis' : 0,
'empty' : 0
}

currentGroup=''
currentSubgroup=''

with open('emoji-list.txt',encoding='utf-8') as f:
    for line in f:

        if line.startswith('#'):

            if line.startswith('# group'):
                counter['groups']+=1
                currentGroup=line.split(": ")[-1].strip()
                emojiDict[currentGroup]=dict()
                #print(currentGroup)

            if line.startswith('# subgroup'):
                counter['subgroups']+=1
                currentSubgroup=line.split(": ")[-1].strip()
                emojiDict[currentGroup][currentSubgroup]=[]
                #print(' ',currentSubgroup)

            else:
                counter['comments']+=1

        elif not line.isspace():
            counter['emojis']+=1
            newEmoji = parseEmoji(line)
            emojiDict[currentGroup][currentSubgroup].append(newEmoji)

        else:
            counter['empty']+=1

print(counter)
print(emojiDict['Smileys & Emotion'])

with open('emoji-list.json','w') as jsonF:
    jsonF.write(json.dumps(emojiDict))