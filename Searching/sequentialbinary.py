import time
import random
import math

def createList(length):
    varList = []

    for x in range(length):
        varList.append(x)

    return varList


def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1

    return found


def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found


def main():
    simList = createList(1000)
    seqElap = time.perf_counter()
    binElap = time.perf_counter()

    for x in range(20):
        searchTarget = random.choice(simList)

        seqStart = time.perf_counter()
        sequentialSearch(simList, searchTarget)
        seqEnd = time.perf_counter()

        binStart = time.perf_counter()
        binarySearch(simList, searchTarget)
        binEnd = time.perf_counter()

        seqElap += seqEnd - seqStart
        binElap += binEnd - binStart

    avgSeqElap = seqElap / 20
    avgBinElap = binElap / 20

    print('Search Test')
    print('20 Tests Done\n')
    print('Average SequentialSearch Elapsed Time: ' + str(round(avgSeqElap, 8)) + 'sec.')
    print('Average BinarySearch Elapsed Time: ' + str(round(avgBinElap, 8)) + 'sec.')

main()