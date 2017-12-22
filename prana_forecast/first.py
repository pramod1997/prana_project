#### python script running 

### file as input 

### 

import pandas as pd
import numpy as np
import dateutil
from datetime import datetime
import math
from plot import plot #### plot file 
from sys import platform as _platform
import os


def months_between(d1, d2):
	d1=datetime.strptime(d1,"%Y-%m-%d %H:%M:%S")
	d2=datetime.strptime(d2,"%Y-%m-%d %H:%M:%S")
	return abs(d1.year-d2.year)*12 + abs(d1.month-d2.month)

def file_summary(file_name):
	if _platform == "linux" or _platform == "linux2":
   		print "linux"
   		path="/home/pramod/Desktop/pranaproject/"
	elif _platform == "darwin":
   		print "linux"
	elif _platform == "win32":
   		print "win32"
   		#### specify different path 

	elif _platform == "win64":
		print "win64"
		#### specify different path
	
	data = pd.read_excel(path+file_name) ### detect .endswith==csv and give otion for that
	header = ['Part','Date','Quantity']
	#data.to_csv('Input.csv', sep='\t', encoding='utf-8', column=header, index= False)

### no of records


	no_of_records = data['Date'].count()



### no of bad records

	bad_records = sum([True for idx,row in data.iterrows() if any(row.isnull())])


#### no of negative records 

	negative = len(data[data['Quantity'].isnull()])


### unnamed records

	unnamed = len(data[data['Part'].isnull()])


### min date 
	mindate = str(data['Date'].min())

### max date

	max_date = str(data['Date'].max())


#### no of parts 

	no_of_parts = len(data['Part'].unique())

#### filling the data where null for timebeing it is left 

	list1=(data['Part'].unique()).tolist()

	part_list =  [str(r) for r in list1]

####calulate partwise cv2 and ADI 
	ADI_list=[]
	CV2_list=[]
	smooth=0
	erratic=0
	lumpy=0
	intermittent=0
##### all are segmented here
	print "the file name supplied to directory is " + file_name
	### process the file name 

	actual_file_name= file_name.split('/')



	if not os.path.exists("/home/pramod/Desktop/pranaproject/prana/Part_"+actual_file_name[1]):
		os.makedirs("/home/pramod/Desktop/pranaproject/prana/Part_"+actual_file_name[1])
	part_no=0;

	for i in part_list:
		part_no=part_no+1
		name = "df"+i
		name = data[data['Part'].notnull() & (data['Part'] == i)]

		part_file_name= "Part_"+str(part_no)+"_"+i 
		print part_file_name

		location_of_part="/home/pramod/Desktop/pranaproject/prana/Part_"+actual_file_name[1]+"/"+part_file_name+".csv"

		name.to_csv(location_of_part, sep='\t', encoding='utf-8', column=header, index= False)




	#### calculation of adi and cv2
		df_date = name['Date'].tolist()
		df_quantity=name['Quantity'].tolist()
		df_date = [str(r) for r in df_date]
		df_quantity=[str(r) for r in df_quantity]
		local_adi=0.0
		local_cv2=0.0

	#### cv2 = stdev / average population
		s = [ int(x) for x in df_quantity ]
		def average(s): return sum(s) * 1.0 / len(s)
		avg = average(s)
		variance = map(lambda x: (x - avg)**2, s)
		standard_deviation = math.sqrt(average(variance)) 
		cv2 = float(standard_deviation/avg)
		CV2_list.append(cv2)

		no_of_records=len(df_date)

		for i in range (1,len(df_date)):  ####update th formula 
			local_adi=local_adi+float(months_between(df_date[i],df_date[i-1]))
		ADI = local_adi/(no_of_records-1)
		####append to ADI list
		ADI_list.append(ADI)

		### classify : 
		if(ADI<1.32 and cv2<0.49):
			smooth=smooth+1
		if(ADI<1.32 and cv2>=0.49):
			intermittent=intermittent+1
	 
		if(ADI>=1.32 and cv2<0.49):
			erratic=erratic+1
	 
		if(ADI>=1.32 and cv2>=0.49):
			lumpy=lumpy+1
	 


	

### plot all the points there on graph by adding extra row of adi and cv2 to them and x nad y axis plot the points


### add caption - Lumpy erratic etc. 

#### generate graph call plot.py



	plot(ADI_list,CV2_list,0,4,0,2)   #### x values and Y values and x range y range


### the return dict  structure : [no,of records , bad records ,neagtive , unnamed , mindate , max date, no of parts , smooth ,inter , erratic , lumpy ,  ]
	return_dict = {}
	return_quantity = ['actual_file_name','no_of_records','bad_records','negative','unnamed','mindate','max_date','no_of_parts','smooth','intermittent','erratic','lumpy']
	return_values=[actual_file_name[1],no_of_records,bad_records,negative,unnamed,mindate,max_date,no_of_parts,smooth,intermittent,erratic,lumpy]
	
	for i in range(len(return_quantity)):
		return_dict[return_quantity[i]] = return_values[i]
	
	return return_dict
	



#### 

 




