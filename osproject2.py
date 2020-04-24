#This is going to be the simulator of a virtual memory page replacements
#algotythems using FIFO.
#Cesar Villanueva- Vazquez  and Nick Mullen
import Queue as queue
import sys
import os
import random
import array

#Global Variables
randNumString = []
frameNum = []
cycles = 30



numberOfPages = 100
#ref string arrar, and ref frame array

#Creating random variables for the array
class StringArray():
    global randNumString

    def run(self):

        for i in range(numberOfPages):
            ranPageNumber = random.randint(0,49)
            randNumString.append(ranPageNumber)


class fifoMethod():
    global randNumString
    global cycles
    
    def run(self):

        print(randNumString)
        print('\n')
        pageFaults = []*30  #keep track of all page faults in 30 cycles
        q = queue.Queue()

        for i in range(cycles):                 #we are running each method 30 times
            virtuMemoryFrames = [-1]*(i + 1)          #to maintain only i amount if frames
            indexJ = -1
            found = False
            currPage = 0                           #flag to exit while loop
            self.fifoPageFault = 0                                            #helps run through virtuMemoryFrames

            for j in range(len(randNumString) - 1):                         # Start going through 100 integer string
                foundFlag = 0
                for k in range(len(virtuMemoryFrames)):    #we can only go through the current amount
                                                           # of frms
                    if randNumString[currPage] == virtuMemoryFrames[k]:#if current page is found go to next
                        currPage += 1                                          #next page and extit current while loop
                        foundFlag = 1
                        break

                if foundFlag == 0:                      #initialize the Virtual Memory List
                    indexJ = (indexJ + 1) % len(virtuMemoryFrames)
                    virtuMemoryFrames[indexJ] = randNumString[currPage]
                    q.put(indexJ)
                    self.fifoPageFault += 1
                    currPage += 1
                    found = True
                                
            pageFaults.append(self.fifoPageFault)    
            

        print('FIFO Page faults')
        print(pageFaults)
####################################################################################################################
###############################################OPTIMAL###############################################
# Optimal Page Replacement Algorithm
class optimalMethod():
    global randNumString
    global cycles
    
    def run(self):
    
        pageFaultTbl = []
        print('\n')
        print(randNumString)
        print('\n')
        
        for i in range(cycles):                      #outer loop
            virtuMemoryFrames = [-1]*(i + 1)          #to maintain only i amount if frames
            currPage = 0      
            pageFaults = 0                     
            
            

            for i in range(len(randNumString)):       #middle loop
                
                foundFlag = 0                       #flag to exit while loop
                for j in range(len(virtuMemoryFrames)):
                    if (virtuMemoryFrames[j] == randNumString[i]):
                        foundFlag = 1
                        break

                if foundFlag == 0:
                    faulted = False
                    newFrame = -1

                    for k in range(len(virtuMemoryFrames)):
                        if virtuMemoryFrames[k] == -1:
                            faulted = True
                            newFrame = k

                    if not faulted:   # find next use farthest page used in future
                        
                        furthest1 = 0
                        farFutureHldr = -1
                        for q in range(len(virtuMemoryFrames)):
                            
                            if virtuMemoryFrames[q] != -1:
                                found = False
                                for m in range(i, len(randNumString) - 1):
                                    if randNumString[m] == virtuMemoryFrames[q]:
                                        found = True
                                        if m > furthest1:
                                            furthest1 = m
                                            farFutureHldr = q
                                        break

                                if not found:
                                    farFutureHldr = q
                                    break

                        faulted = True
                        newFrame = farFutureHldr

                    pageFaults += 1
                    virtuMemoryFrames[newFrame] = randNumString[i]
                    
            pageFaultTbl.append(pageFaults)          
            
        print('Optimal Page Faults')
        print(pageFaultTbl)



