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
    global frameNum


    def run(self):

        for i in range(numberOfPages):
            ranPageNumber = random.randint(0,49)
            randNumString.append(ranPageNumber)


class fifoMethod():
    global randNumString
    global frameNum

    def run(self):

        currPage = 0
        pageFaults = []*30  #keep track of all page faults in 30 cycles
        
        q = queue.Queue()

        for i in range(cycles - 1):                 #we are running each method 30 times
            virtuMemoryFrames = [-1]*(i + 1)          #to maintain only i amount if frames
            found = False                           #flag to exit while loop
            self.fifoPageFault = 0                                            #helps run through virtuMemoryFrames

            for j in range(len(randNumString) - 1):                         # Start going through 100 integer string
                indexJ = 0

                for k in range(len(virtuMemoryFrames)):    #we can only go through the current amount
                    foundFlag = 0
                                                                              # of frms
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
                        self.fifoPageFault +=1
            
            pageFaults[i] = self.fifoPageFault    
            #print(self.fifoPageFault, "current cycle", i)
####################################################################################################################
###############################################OPTIMAL###############################################
# Optimal Page Replacement Algorithm
# def __optimal():
#     global a, n, m
#     x = 0
#     page_faults = 0
#     page = []
#     FREE = -1
#     for i in range(m):
#         page.append(FREE)
#
#     for i in range(n):
#         flag = 0
#         for j in range(m):
#             if (page[j] == a[i]):
#                 flag = 1
#                 break
#
#         if flag == 0:
#             # look for an empty one
#             faulted = False
#             new_slot = FREE
#             for q in range(m):
#                 if page[q] == FREE:
#                     faulted = True
#                     new_slot = q
#
#             if not faulted:
#                 # find next use farthest in future
#                 max_future = 0
#                 max_future_q = FREE
#                 for q in range(m):
#                     if page[q] != FREE:
#                         found = False
#                         for ii in range(i, n):
#                             if a[ii] == page[q]:
#                                 found = True
#                                 if ii > max_future:
#                                     # print "\n\tFound what will be used last: a[%d] = %d" % (ii, a[ii]),
#                                     max_future = ii
#                                     max_future_q = q
#
#                                 break
#
#                         if not found:
#                             # print "\n\t%d isn't used again." % (page[q]),
#                             max_future_q = q
#                             break
#
#                 faulted = True
#                 new_slot = max_future_q
#
#             page_faults += 1
#             page[new_slot] = a[i]
#             print
#             "\n%d ->" % (a[i]),
#             for j in range(m):
#                 if page[j] != FREE:
#                     print
#                     page[j],
#                 else:
#                     print
#                     "-",
#         else:
#             print
#             "\n%d -> No Page Fault" % (a[i]),
#
#     print
#     "\n Total page faults : %d." % (page_faults)



