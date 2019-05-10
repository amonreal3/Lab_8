"""
Adrian Monreal
olac fuentes cs2302
Lab 8

"""
from math import *
import time
import math
import random
import numpy as np


"""
#1
(Randomized algorithms) Write a program to ”discover” trigonometric identities. 
Your program should test all combinations of the trigonometric expressions shown below and use a 
randomized algorithm to detect the equalities. For your equality testing, 
generate random numbers in the −π to π range.
"""
"""
i created an function that creates an array or list that multiplies t to every function
then i called it to this function to traverse it, i passed a list of strings for display purposes
i also made sure j was always 1 more than i so that way it wouldn't check against itself

"""

def Randomized_Algorithms(trigID): #array of trig identies
    t =  random.uniform(-math.pi,math.pi)
    print ("your random number between -pi and pi", t)
    trigArray = fill_trig_array(t)
    print(trigArray)
    for i in range(len(trigArray)):
        j=i+1
        while j != len(trigArray):
            if trigArray[i] == trigArray[j]:
                print(trigID[i],"=",trigArray[i], "is equal to ", trigID[j],"=",trigArray[j], "when t is ", t)
            j+=1


"""
    0 = sin(t) | 1= cos(t) |2= tan(t)| 3=sec(t)| 4 = −sin(t)
    5 =  −cos(t)| 6 =  −tan(t)| 7 = sin(−t)| 8 = cos(−t)|
     9 = tan(−t)| 10= (sin(t) /cos(t))| 11=(2sin(t/2)cos(t/2))
    12 = (sin^2(t))| 13 = (1 − cos^2 (t))| 14= (( 1−cos(2t))/2)
    15(1/(cos(t)))
"""
def fill_trig_array(t):
    trigArray = []
    trigArray.append(math.sin(t))
    trigArray.append(math.cos(t))
    trigArray.append(math.tan(t))
    trigArray.append(1/(math.sin(t)))
    trigArray.append(-math.sin(t))
    trigArray.append(-math.cos(t))
    trigArray.append(-math.tan(t))
    trigArray.append(math.sin(-t))
    trigArray.append(math.cos(-t))
    trigArray.append(math.tan(-t))
    trigArray.append(((math.sin(t)) /(math.cos(t))))
    trigArray.append((2*math.sin(t/2) * math.cos(t/2)))
    trigArray.append(math.pow(math.sin(t), 2))
    trigArray.append((1-(math.pow(math.cos(t),2))))
    trigArray.append(((1-(math.cos(2*t)))/2))
    trigArray.append((1/(math.cos(t))))
    return trigArray
"_____________________________________________________________"

"""
#2
(Backtracking) The partition problem consists of determining if there is a way to partition a set of integers S
 into two subsets S1 and S2 such that 􏰁S1 = 􏰁S2. 
 Recall that S1 and S2 are a partition of S if and only if S1 ∪ S2 = S and S1 ∩ S2 = {}.
  Write a function that solves the partition problem using backtracking. If a partition exists, 
  your program should display it; otherwise it should indicate that no partition exists. 
  For example, if S = {2, 4, 5, 9, 12}, your program should output the partition S1 = {2, 5, 9} 
  and S2 = {4, 12} and if S = {2, 4, 5, 9, 13} your program should indicate that no partition exists.
"""
def SetEven(s):
    count = 0
    for i in range(len(s)):
        count = count + s[i]
    if count % 2 == 1:
        return False
    else:
        return True

def subsetsum(S,last,goal):
    if goal ==0:
        return True, []
    if goal<0 or last<0:
        return False, []
    res, subset = subsetsum(S,last-1,goal-S[last]) # Take S[last]
    if res:
        subset.append(S[last])
        return True, subset
    else:
        return subsetsum(S,last-1,goal) # Don't take S[last]
"""
this function uses subsetsum to see if a list of elements can be partitioned
it checks if it can by first checking if its odd or even if its odd it knows automatically 
that it can so it prints no partion exist and None
but if it can it inputs half the list in one set and then test which elements are in the first one
and if they are not then add them to a second list 
then it checks if both sums are the same if they are return the list if not display there are no partition
"""
def backtracking(S):
    if sum(S) % 2 == 1:
        print("No Partition exist")
        return None

    else:
        t = sum(S)
        a,s1 = subsetsum(S,len(S)-1,t/2)
        s2 = []

        for i in range(len(S)):
            if S[i] not in s1:
                s2.append(s[i])
        if sum(s1) != sum(s2):
            print("no partition exist")
        else:
            return s1,s2

"_________________________________________________"
TrigIDs = ["sin(t)", "cos(t)", "tan(t)","sec(t)","−sin(t)", "−cos(t)",
           " −tan(t)","sin(−t)","cos(−t)","9 = tan(−t)","(sin(t) /cos(t))","(2sin(t/2)cos(t/2))",
           "(sin^2(t))","(1 − cos^2 (t))","(( 1−cos(2t))/2)","(1/(cos(t)))"]
s = [2,4,6,10,15]
Randomized_Algorithms(TrigIDs)
print(backtracking(s))

