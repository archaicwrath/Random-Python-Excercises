import random as rand
import queue
import victim

namelist = ["Linda","James","Mary","Robert","Patricia","John","Barbara","Michael","Susan","David","Nancy","William",
            "Deborah","Richard","Sandra","Thomas","Carol","Charles","Kathleen","Gary","Sharon","Larry","Karen","Ronald",
            "Donna","Joseph","Brenda","Donald","Margaret","Kenneth","Diane","Steven","Pamela","Dennis","Janet","Paul",
            "Shirley","Stephen","Carolyn","George","Judith","Daniel","Janice","Edward","Cynthia","Mark","Elizabeth",
            "Jerry","Judy","Gregory","Betty","Bruce","Joyce","Roger","Christine","Douglas","Cheryl","Frank","Gloria",
            "Terry","Beverly","Raymond","Martha","Timothy","Bonnie"]

# Global Variables
victimQueue = queue.Queue()
iter = 30

itSpeed = 0
gooseSpeed = 0


for i in range(iter):
    grpSize = rand.randrange(5, 50)
    grpDiv = 2

    for i in range(grpSize):
        newVic = victim.Victim()
        newVic.setName(rand.choice(namelist))
        newVic.setSpeed(rand.uniform(0, 1))
        victimQueue.enqueue(newVic)

    size = victimQueue.size()
    it = victimQueue.dequeue()
    iterations = rand.randrange(int(grpSize / grpDiv), int(grpSize * grpDiv))

    for d in range(iterations):
        duck = victimQueue.dequeue()
        # print(duck.getName() + " -> DUCK.")
        victimQueue.enqueue(duck)

    goose = victimQueue.dequeue()

    itSpeed = it.getSpeed()
    gooseSpeed = goose.getSpeed()
    print("Runner: " + it.getName() + "\t\tGoose: " + goose.getName())

    if it.getSpeed() > goose.getSpeed():
        victimQueue.enqueue(it)
        print(goose.getName() + " loses.")
    else:
        victimQueue.enqueue(goose)
        print(it.getName() + " loses.")

    print("Runner speed: " + str(round(itSpeed, 3)) + "\tGoose speed: " + str(round(gooseSpeed, 3)) + "\tNumber of Iteration
