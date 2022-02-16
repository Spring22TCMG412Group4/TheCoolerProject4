# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 22:50:49 2022

@author: Matthew Nagbe
"""

DataList =[["Requests last 6 months",1269837],["Requests overall",63779890]]





print (" Requests from log file sorted ")

for item in DataList:
    print(":",item[0]," "*(22-len(str(item[0]))),":",item[1]," "*(-len(str(item[1]))))
         
