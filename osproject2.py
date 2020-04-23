#This is going to be the simulator of a virtual memory page replacements
#algotythems using FIFO.
#Cesar Villanueva- Vazquez  and Nick Mullen

import sys
import os
import random
import array
import queue

#Global Variables
randNumString = []
frameNum = []
cycles = 30

numberOfPages = 100
#ref string arrar, and ref frame array

#Creating random variables for the array
class StringArray():
    global randNumString
    global frameNum


    def run(self):

        for i in range(numberOfPages):
            ranPageNumber = random.randint(0,49)
            randNumString.append(ranPageNumber)

class fifoMethod():
    global randNumString
    global frameNum

    def __init__(self, cycle, target, pageFault ):

        self.currCycle = cycle
        self.currTarget = target
        self.fifoPageFault = pageFault

    def run(self):

        currPage = 0
        self.fifoPageFault = 0
        q = queue.Queue()

        for i in range(cycles - 1):                 #we are running each method 30 times
            virtuMemoryFrames = [-1]*(i + 1)          #to maintain only i amount if frames
            found = False                           #flag to exit while loop
                                      #helps run through virtuMemoryFrames


            for j in range(len(randNumString) - 1):                         # Start going through 100 integer string
                indexJ = 0

                while found != True or indexJ >= len(virtuMemoryFrames):    #we can only go through the current amount
                    print("hello")                                                     # of frms
                    if virtuMemoryFrames[indexJ] == -1:                      #initialize the Virtual Memory List
                        virtuMemoryFrames[j] = randNumString[currPage]
                        q.put(indexJ)
                        self.fifoPageFault += 1
                        currPage += 1
                        found = True

                    elif randNumString[currPage] == virtuMemoryFrames[indexJ]:#if current page is found go to next
                        currPage += 1                                          #next page and extit current while loop
                        found = True

                    elif indexJ == len(virtuMemoryFrames) - 1:                #make function for when it end ofMemframes
                        virtuMemoryFrames[q.get()] = randNumString[currPage]
                        self.fifoPageFault += 1

                    else:
                        indexJ += 1



