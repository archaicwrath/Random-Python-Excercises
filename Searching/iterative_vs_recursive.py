import datetime
import random
import math


def createRandomList(size):
    rlist = [random.randint(x, math.floor(random.randint(x, math.floor(x * math.e)))) for x in range(size)]
    return sorted(rlist)


def iterativeBinarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
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

def simulateSearches(reps, maxLen):
    elapsedTimes = []

    for c in range(reps):
        testlist = createRandomList(random.randint(1, maxLen))
        testsearch = testlist[random.randint(0, len(testlist) - 1)]

        iterStart = datetime.datetime.now()
        iterativeBinarySearch(testlist, testsearch)
        iterEnd = datetime.datetime.now()

        iterElapsed = iterEnd - iterStart
        iterElapsed = iterElapsed.total_seconds()

        recurStart = datetime.datetime.now()
        recursiveBinarySearch(testlist, testsearch)
        recurEnd = datetime.datetime.now()

        recurElapsed = recurEnd - recurStart
        recurElapsed = recurElapsed.total_seconds()

        elapsedTimes.append([len(testlist), testlist.index(testsearch), iterElapsed, recurElapsed])

    return elapsedTimes


def main():
    amnt = random.randint(10, 50)
    simList = simulateSearches(amnt, 100000)

    simLen = [x[0] for x in simList]
    simPos = [x[1] for x in simList]
    simIterEl = [x[2] for x in simList]
    simRecEl = [x[3] for x in simList]

    print('--- Search Test ---')
    print('Number of simulations:', amnt)
    print('Average List Size: ' + str(math.ceil(sum(simLen)/len(simLen))))
    print('Average search target distance: ' + str(math.ceil(sum(simPos)/len(simPos))) + '\n')
    print('Average iterative search elapsed time: ' + str(sum(simIterEl)/len(simIterEl)) + ' sec.')
    print('Average recursive search elapsed time: ' + str(sum(simRecEl)/len(simRecEl)) + ' sec.')

    # I would reason that with the recursive search, the amount of memory allocated to the recursive function increases
    # as n number of searches increases. Unlike with the iterative search, which allocates and then de-allocates memory
    # as the search function is called, each subsequent layer of recursion stays open, increasing memory overhead. This
    # should be where the different in time elapsed comes from, regardless of hardware architecture.


if __name__ == '__main__':
    main()