import time
import random


def createList(length):
    varList = []

    for x in range(length):
        varList.append(x)

    return varList


def iterativeBinarySearch(alist, item):
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


def recursiveBinarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return recursiveBinarySearch(alist[:midpoint], item)
            else:
                return recursiveBinarySearch(alist[midpoint+1:], item)


def main():
    simList = createList(1000)
    iterElap = time.perf_counter()
    recurElap = time.perf_counter()

    for x in range(20):
        searchTarget = random.choice(simList)

        iterStart = time.perf_counter()
        iterativeBinarySearch(simList, searchTarget)
        iterEnd = time.perf_counter()

        recurStart = time.perf_counter()
        recursiveBinarySearch(simList, searchTarget)
        recurEnd = time.perf_counter()

        iterElap += iterStart - iterEnd
        recurElap += recurStart - recurEnd

    avgIterElap = iterElap / 20
    avgRecurElap = recurElap / 20

    print('Search Test')
    print('20 Tests Done\n')
    print('Average iterativeBinarySearch Elapsed Time: ' + str(round(avgIterElap, 8)) + 'sec.')
    print('Average recursiveBinarySearch Elapsed Time: ' + str(round(avgRecurElap, 8)) + 'sec.')

main()