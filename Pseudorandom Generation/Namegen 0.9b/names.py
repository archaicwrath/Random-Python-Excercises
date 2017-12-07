import random

cList = ['b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'r', 's', 't', 'v']
vList = ['a', 'e', 'i', 'o', 'u']
ccList = ['br', 'dr', 'mh', 'vh', 'kr', 'zr', 'zh', 'th', 'tr', 'tl', 'zl', 'fr', 'ph']
vvList = ['ae', 'ai', 'ia', 'ya', 'ea', 'ia', 'ei', 'ie']
cvList = [cons+vowel for cons in cList for vowel in vList]
vcList = [vowel+cons for vowel in vList for cons in cList]


def splitString(nSeed):
    nList = []
    if len(nSeed) % 2 == 0:
        tempStart = nSeed[0]
        tempEnd = nSeed[len(nSeed) - 1]
        temp = nSeed[1:len(nSeed)-2]
        tempList = [temp[i:i + 2] for i in range(0, len(temp), 2)]
        nList.append(tempStart)
        nList.extend(tempList)
        nList.append(tempEnd)
    else:
        tempStart = nSeed[0]
        tempList = [nSeed[i:i + 2] for i in range(1, len(nSeed), 2)]
        nList.append(tempStart)
        nList.extend(tempList)
    return nList


def generateName(nSeed):
    nList = splitString(nSeed)
    characters = []

    for val in nList:
        if val == 'C':
            characters.append(random.choice(cList))
        elif val == 'V':
            characters.append(random.choice(vList))
        elif val == 'CV':
            characters.append(random.choice(cvList))
        elif val == 'VC':
            characters.append(random.choice(vcList))
        elif val == 'CC':
            characters.append(random.choice(ccList))
        elif val == 'VV':
            characters.append(random.choice(vvList))

    return ''.join(characters)


def main():
    for i in range(10):
        print(generateName('CVCVV'))

if __name__ == '__main__':
    main()