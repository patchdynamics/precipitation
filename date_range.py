def daterange(start_date, end_date):
	  for n in range(int ((end_date - start_date).days)):
			    yield start_date + datetime.timedelta(n)
