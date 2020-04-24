#This is going to be the simulator of a virtual memory page replacements
#algotythems.
#Cesar Villanueva- Vazquez  and Nick Mullen

import sys
import os
import random
randNumString = []
frameNum = []
frameCount = []
pageFaultData = []
#ref string arrar, and ref frame array


def LRU():

    #Counts page faults
    pageFault = 0

    #total number of frames
    currentNumOfFrames = 1

    #Keeps track of the age of each frame
    frameAge = []

    #Increases number of frames from 1 to 30
    while currentNumOfFrames <= 30:

        #Iterates through ref. string until all
        #frames are filled with non matching values
        for i in range(len(randNumString)):
            if (len(frameNum) < currentNumOfFrames):
                if (randNumString[i] not in frameNum):
                                  
                    #appends new value into frame list
                    frameNum.append(randNumString[i])

                    #Appends a spot for frameAge
                    frameAge.append(0)

                    #increments all current spots in frameAge
                    for j in range(len(frameAge) - 1):
                        frameAge[j] = frameAge[j] + 1

                    #counts up minimum number of page faults per frame loop
                    pageFault = pageFault + 1

                #Adjusts LRU weights if there is a hit
                elif (randNumString[i] in frameNum):
                    foundIndex = frameNum.index(randNumString[i])
                    for j in range(len(frameNum)):
                        
                        #Only increment frames that are younger than replaced index
                        if (frameAge[j] < frameAge[foundIndex]):
                            frameAge[j] = frameAge[j] + 1
                    
                    #Reset found Index to youngest
                    frameAge[foundIndex] = 0

            #Logic after frames are filled
            #Adjusts LRU weights if there is a hit
            elif (randNumString[i] in frameNum):
                foundIndex = frameNum.index(randNumString[i])
                
                #Only increment frames younger than replaced index
                for j in range(len(frameNum)):
                    if (frameAge[j] < frameAge[foundIndex]):
                        frameAge[j] = frameAge[j] + 1
                
                #Reset found Index to youngest
                frameAge[foundIndex] = 0
            
            #Miss logic: Find oldest index -> Replace frameNum[oldest] w/ next string ->
            # -> increment all younger frames -> set index to youngest
            else:
                oldestIndex = frameAge.index(max(frameAge))
                frameNum[oldestIndex] = randNumString[i]
                
                for j in range(len(frameNum)):
                        frameAge[j] = frameAge[j] + 1
                
                frameAge[oldestIndex] = 0
                pageFault = pageFault + 1
            #print("\nframeNum = " + str(frameNum))
            #print("frameAge = " + str(frameAge))
 
       
        print("frameNum = " + str(frameNum))
        print("frameAge = " + str(frameAge))
        print("pageFaults = " + str(pageFault) + '\n')
        
        pageFaultData.append(pageFault)
        frameNum.clear()
        frameAge.clear()
        pageFault = 0
        currentNumOfFrames = currentNumOfFrames + 1

def main():
     #Auto generates the two lists with values
    i = 0
    while i < 100:
        page = random.randint(0,49)
        randNumString.append(page)
        
        if (i >= 1 and i <= 30):
            frameCount.append(i)

        i = i + 1
    
    print(randNumString)
    LRU()

    print(frameCount)
    print(pageFaultData)







main()
