import datetime
import random
import math


def createRandomList(size):
    rlist = [random.randint(x, math.floor(random.randint(x, math.floor(x * math.e)))) for x in range(size)]
    return sorted(rlist)


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


def simulateSearches(reps, maxLen):
    elapsedTimes = []

    for c in range(reps):
        testlist = createRandomList(random.randint(1, maxLen))
        testsearch = testlist[random.randint(0, len(testlist) - 1)]

        seqStart = datetime.datetime.now()
        sequentialSearch(testlist, testsearch)
        seqEnd = datetime.datetime.now()

        seqElapsed = seqEnd - seqStart
        seqElapsed = seqElapsed.total_seconds()

        binStart = datetime.datetime.now()
        binarySearch(testlist, testsearch)
        binEnd = datetime.datetime.now()

        binElapsed = binEnd - binStart
        binElapsed = binElapsed.total_seconds()

        elapsedTimes.append([len(testlist), testlist.index(testsearch), seqElapsed, binElapsed])

    return elapsedTimes


def main():
    amnt = random.randint(10, 50)
    simList = simulateSearches(amnt, 100000)

    simLen = [x[0] for x in simList]
    simPos = [x[1] for x in simList]
    simSeqEl = [x[2] for x in simList]
    simBinEl = [x[3] for x in simList]

    print('--- Search Test ---')
    print('Number of simulations:', amnt)
    print('Average List Size: ' + str(math.ceil(sum(simLen)/len(simLen))))
    print('Average search target distance: ' + str(math.ceil(sum(simPos)/len(simPos))) + '\n')
    print('Average sequential search elapsed time: ' + str(sum(simSeqEl)/len(simSeqEl)) + ' sec.')
    print('Average binary search elapsed time: ' + str(sum(simBinEl)/len(simBinEl)) + ' sec.')


if __name__ == '__main__':
    main()