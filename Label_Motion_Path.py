#reads dataframe from .csv that user specifies.
#cycles though dataframe and adds the data for when the teach point is changing from its previous point to its new teach point effectivly labeling the motion path.

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

root.filename = filedialog.askopenfilename(initialdir = "C:/Users/"+user_name+"/Desktop/", title = "Select File For Controller Data To Be Labeled")
openThisFile = root.filename
dataFrameJointXYTP = pd.read_csv(openThisFile)
PointFrom = 999
PointTo = 999
dataFrameJointXYTP["PointFrom"] = "PointFrom"
dataFrameJointXYTP["PointTo"] = "PointTo"
dataFrameJointXYTP["PATH"] = "PointFrom_PointTo_Iteration"

for i in range(len(dataFrameJointXYTP)):
	if dataFrameJointXYTP["Teach_Point"][i] != 999:
		PointFrom = dataFrameJointXYTP["Teach_Point"][i]
	dataFrameJointXYTP["PointFrom"][i] = PointFrom
	print("Teach Point From: "+str(i)+" OF "+str(len(dataFrameJointXYTP)))

for j in range(len(dataFrameJointXYTP)-1, 1, -1):
	if dataFrameJointXYTP["Teach_Point"][j] != 999:
		PointTo = dataFrameJointXYTP["Teach_Point"][j]
	dataFrameJointXYTP["PointTo"][j] = PointTo
	print("Teach Point To: "+str(j)+" OF "+str(len(dataFrameJointXYTP)))

for k in range(len(dataFrameJointXYTP)):
	if dataFrameJointXYTP["PointFrom"][k] == dataFrameJointXYTP["PointTo"][k]:
		dataFrameJointXYTP["PATH"][k] = ("P"+str(dataFrameJointXYTP["PointFrom"][k]))
		print("Teach Point From/To: "+str(k)+" OF "+str(len(dataFrameJointXYTP)))
	else:
		dataFrameJointXYTP["PATH"][k] = ("P"+str(dataFrameJointXYTP["PointFrom"][k])+"->P"+str(dataFrameJointXYTP["PointTo"][k]))
		print("Teach Point From/To: "+str(k)+" OF "+str(len(dataFrameJointXYTP)))

dataFrameJointXYTP = dataFrameJointXYTP.drop(["Teach_Point", "PointFrom", "PointTo"], axis=1)

result = dataFrameJointXYTP
result.to_csv("C:/Users/"+user_name+"/Desktop/PATH_"+today+".csv")
