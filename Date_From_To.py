#Allows user to trim data to specific time and range.

import pandas as pd
from tkinter import filedialog
from tkinter import *
import os
import numpy as np
import math
user_name = os.environ.get("USERNAME")
today = date.today()
root = Tk()
root.wm_state('iconic')

root.filename = filedialog.askopenfilename(initialdir = "C:/Users/"+user_name+"/Desktop/", title = "Select File For Small Data Set Data")
openThisFile = root.filename
dataFrameTrainingData = pd.read_csv(openThisFile)
dataFrameTrainingData

dataFrameTrainingData = dataFrameTrainingData[dataFrameTrainingData['Time_Stamp'].between("2022-09-30 15:00","2022-09-30 16:00")]


result = dataFrameTrainingData
result.to_csv("C:/Users/"+user_name+"/Desktop/PATH_"+today+"_TrainData.csv")