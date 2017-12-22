

def bestfit(filename):  ### a part file is assigned to it 
	print "best fit method executed  "
	print "file name  sent " + filename

	### return the best mape filename its axis values range values , ,  store in forecast_<file_name>_<bestfit>
	x_min=0
	x_max=0
	y_min=0
	y_max =0
	x_list =[] 
	y_list = []

	best_fit_dict = {'x_list':x_list, 'y_list': y_list ,'filename': filename , 'x_min': x_min , 'x_max': x_max, 'y_min':y_min, 'y_max':y_max}
	

	return best_fit_dict 








	

	





