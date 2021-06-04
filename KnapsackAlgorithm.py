# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 22:04:56 2021

@author: Omar Wael
"""
def knapsackAlgo(typeAlgorithm,costFunction,constraint,numberOfObjects,objectDic):
      #i will implement it unsing 0/1 and max profit to hangover deadline
      totalWeight = 0
      totalProfit = 0
      if costFunction == 1 : #max profit
          objectDic = maxProfit(objectDic)
          print(objectDic)
      elif costFunction==2: #min weight
          objectDic = minWeight(objectDic)
          print("min weight",objectDic)
      elif costFunction==3: #profit per weight
         objectDic = profitPerWeight(objectDic)
         print("profit per weight",objectDic)
        
      if typeAlgorithm == 0:
          totalProfit,totalWeight = Fractional(objectDic,totalWeight,totalProfit,constraint)   
          print("case fractional")
      else: 
          totalProfit,totalWeight = nonFractional(objectDic,totalWeight,totalProfit,constraint)
          print("case nonFractional")
        
      print(totalWeight)
      return totalProfit
#def calculateProfitPerWeight():
 #       return 0 
def maxProfit(objectDic): 
   return dict(sorted(objectDic.items(), key=lambda item: item[1], reverse=True))

def minWeight(objectDic):
    return  dict(sorted(objectDic.items(), key=lambda item: item[1]))
     
def profitPerWeight(objectDic):
      #put profit per weight instead of profit
     for i in objectDic.keys():
         objectDic[i][1] = objectDic[i][1]/objectDic[i][0]
     return dict(sorted(objectDic.items(), key=lambda item: item[1], reverse=True))
     
def Fractional(objectDic,totalWeight,totalProfit,constraint):
     for i in objectDic.keys():
          totalWeight += objectDic[i][0]
          totalProfit += objectDic[i][1]
          #case fraction = nonfraction
          if totalWeight == constraint:
              break
          if totalWeight > constraint:
              neededWeight = totalWeight - constraint
              remainingWeight = objectDic[i][0]-neededWeight
              totalWeight -= objectDic[i][0]-remainingWeight
              totalProfit -=  objectDic[i][1]/remainingWeight
              break
     return totalProfit,totalWeight
 
def nonFractional(objectDic,totalWeight,totalProfit,constraint):
     for i in objectDic.keys():
          totalWeight += objectDic[i][0]
          totalProfit += objectDic[i][1]
          if totalWeight > constraint:
              totalWeight -=  objectDic[i][0]
              totalProfit -=  objectDic[i][1]
              continue
     return totalProfit,totalWeight
    
def start():
    typeAlgorithm = int(input("Enter 0 for Fractional Knapsack & 1 for 0/1 Knapsack : "))
    costFunction = int(input("choose 1:Maximum Profit - 2:Minimum Weight - 3:Maximum Profit/Weight - 4:All : "))
    numberOfObjects = int(input("Enter number of your objects : "))
    objectDic = {} #first values i weight and second is value
    for i in range(numberOfObjects):
            objectDic[i] = [int(input("Enter weight of object "+str(i)+"  : ")),int(input("Enter value of object "+str(i)+"  : "))]
    constraint = int(input("Enter maximum weight of the knapsack : "))
    #objectDic = {0:[1,5],1:[3,10],2:[5,15],3:[4,7],4:[1,8],5:[4,9],6:[2,4]} 
    print(knapsackAlgo(typeAlgorithm,costFunction,constraint,numberOfObjects,objectDic))
   
exitFlag = 0
while not exitFlag: 
   start()
   exitFlag = int(input("if you want to exit enter 1 or 0 for continue : "))
