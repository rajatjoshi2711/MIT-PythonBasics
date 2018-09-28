# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 22:45:42 2018

@author: Rajat
"""



#Functions example
def addNumbers(firstNum, secondNum):
    sum = firstNum+secondNum
    return sum

firstNumber = 10
secondNumber = 20
sum = addNumbers(firstNumber, secondNumber)
print(sum)



#Functions hands on
def getNameAge(name, age):
    print("Hi!! This is ", name, "; and I'm ", age," years old.")
    
name = "ABC"
age = 21
getNameAge(name, age)

