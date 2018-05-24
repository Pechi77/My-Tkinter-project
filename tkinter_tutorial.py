# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 12:39:59 2017

@author: PA5027251
tkinter turorial
"""

#from tkinter import *
#class Window(Frame):
#
#    def __init__(self, master=None):
#        Frame.__init__(self, master)               
#        self.master = master
#    
#root = Tk()
#app = Windows(root)
#
#root.mainloop()
#import os
#cwd = os.getcwd()
#
#print(cwd)
import ntpath
import os
print (os.path.basename("G:\\test\\Scenario_ExportData-testcase.xlsx"))
aa=ntpath.basename("G:\\test\\Scenario_ExportData-testcase.xlsx")
print(aa)