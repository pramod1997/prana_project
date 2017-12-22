### Note : requires installation of bokeh libray python library for analysis
### installation steps are : 
### pip3 install bokeh
### in python terminal : import bokeh.sampledata
###                    : bokeh.sampledata.download()



from bokeh.plotting import figure , show, output_file ,save
from bokeh.models import HoverTool
from bokeh.models import Range1d

import pandas as pd 
import numpy as np 
from sys import platform as _platform


def plot(x_list,y_list,x_min,x_max,y_min,y_max):
	
	if _platform == "linux" or _platform == "linux2":
   		print "linux"
   		output_file('/home/pramod/Desktop/pranaproject/static/prana_forecast/plot_file_summary.html')   ### the html file which will conatin the plot
	elif _platform == "darwin":
   		print "linux"
	elif _platform == "win32":
   		print "win32"
   		#### specify different path 

	elif _platform == "win64":
		print "win64"
		#### specify different path 




	

#read the csv file and import the data
#df = pd.read_csv('/home/pramod/Desktop/HONORS/shampoo-sales.csv')

#some random data
	x_values=x_list                         ### x axis values 

	y_values=y_list
							### y axis values 

	p = figure(plot_width= 500 , plot_height= 500, tools= 'hover',x_axis_label='X label' , title='Some Title')	
	p.yaxis.axis_label = "Y Lable"                  ### label for Y axis 

	p.x_range = Range1d(x_min,x_max)
	p.y_range = Range1d(y_min,y_max)
	p.scatter( x=x_values, y =y_values)             ### scatter plot or anything like circle , line

	hover = HoverTool                               ### on hovering display the data in a box  
	hover.tooltips=[
	("X" , "@x"),
	("Y", "@y"),
	]

	save(p) 										###  display the graph 
