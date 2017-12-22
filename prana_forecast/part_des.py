#### this file upon input of file name will look 
####into repsective part folder and pull out its description
### for screen2.html


#### following quantities are returned 

import pandas as pd
import numpy as np
import dateutil
from datetime import datetime
import math
from plot import plot #### plot file 
from sys import platform as _platform
import os
from os import listdir

def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]


def part_des(file_name,serial_no):

	### go to the file and compute following quantities
	serial_no=serial_no   ### this is a string
	part_no="0"
	no_of_records=0
	zero="0"
	ADI="0"
	COV2="0"
	type_of_part="0"

	actual_file_name=file_name.split('/')
	actual_file_name = [str(r) for r in actual_file_name]

	### the actual file is in actual_file_name[1]

	### so the file to read will be 

	path="/home/pramod/Desktop/pranaproject/prana/Part_"+actual_file_name[1]

	filenames = find_csv_filenames(path)
	for name in filenames:
  		file_serial_no=name.split('_')
  		print file_serial_no[1], str(serial_no)
  		if file_serial_no[1] == str(serial_no):
  			part_file_to_be_processed=name
  			   #### this gives all the file name in the folder
  			break

  		## process  the file here  fiel name in part_file_to_be_prcocesed and path in path









	return_dict = {}
	return_quantity = ['serial_no','part_no','no_of_records','zero','ADI','COV2','type_of_part']
	return_values=[serial_no,part_no,no_of_records,zero,ADI,COV2,type_of_part]
	
	for i in range(len(return_quantity)):
		return_dict[return_quantity[i]] = return_values[i]
	
	return return_dict


	











