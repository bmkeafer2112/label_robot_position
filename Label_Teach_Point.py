#reads dataframe from .csv that user specifies.
#cycles though dataframe and adds the number associated with teachpoint data from the teach point file where the data is found to be matching within a givin tolerence.

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

root.filename = filedialog.askopenfilename(initialdir = "C:/Users/"+user_name+"/Desktop/", title = "Select File For Controller Data")
openThisFile = root.filename
dataFrameJointXY = pd.read_csv(openThisFile)
dataFrameJointXY = dataFrameJointXY.head(18000)

root.filename = filedialog.askopenfilename(initialdir = "C:/Users/"+user_name+"/Desktop/", title = "Select File For TP Data")
openThisFile = root.filename
dataFrameTP = pd.read_csv(openThisFile)

dataFrameJointXY["Teach_Point"] = 999

TPs = range(1, 150)
for some_Number in TPs:
	some_Number_X = dataFrameTP["TCP_Current_x"][some_Number]
	some_Number_Y = dataFrameTP["TCP_Current_y"][some_Number]
	some_Number_Z = dataFrameTP["TCP_Current_z"][some_Number]
	some_Number_RX = dataFrameTP["TCP_Current_rx"][some_Number]
	some_Number_RY = dataFrameTP["TCP_Current_ry"][some_Number]
	some_Number_RZ = dataFrameTP["TCP_Current_rz"][some_Number]

	for i in range(len(dataFrameJointXY)):
		if math.isclose(dataFrameJointXY["TCP_Current_x"][i], some_Number_X, rel_tol = 0.1) & math.isclose(dataFrameJointXY["TCP_Current_y"][i], some_Number_Y, rel_tol = 0.1) & math.isclose(dataFrameJointXY["TCP_Current_z"][i], some_Number_Z, rel_tol = 0.1) & math.isclose(dataFrameJointXY["TCP_Current_rx"][i], some_Number_RX, rel_tol = 0.1) & math.isclose(dataFrameJointXY["TCP_Current_ry"][i], some_Number_RY, rel_tol = 0.1) & math.isclose(dataFrameJointXY["TCP_Current_rz"][i], some_Number_RZ, rel_tol = 0.1):
			dataFrameJointXY["Teach_Point"][i] = some_Number
			print("Teach Point:" + str(some_Number)+ ", Data Point:" +str(i) + "of" +  str(len(dataFrameJointXY))+ ", Percent Complete:"+str(100*(i/len(dataFrameJointXY))))
		else:
			print("Teach Point:" + str(some_Number)+ " not found, Data Point:" +str(i) + "of" +  str(len(dataFrameJointXY))+ ", Percent Complete:"+str(100*(i/len(dataFrameJointXY))))

result = dataFrameJointXY.query('`Teach_Point` != 999')
result.to_csv("C:/Users/"+user_name+"/Desktop/TP_"+today+"_.csv")
