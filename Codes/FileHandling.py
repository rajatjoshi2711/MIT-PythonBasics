# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 23:13:20 2018

@author: Rajat
"""


#File handling example
f1 = open("sampleFile.txt", 'r')
contents = f1.read()
print(contents)
f1.close()


f2 = open("sampleFileWrite.txt", 'w')
f2.write("This is written by me.")
f2.close()


f3 = open("sampleFileAppend.txt", 'a')
f3.write("Appended text")
f3.close()

