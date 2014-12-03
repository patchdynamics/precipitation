import datetime
import time

def daterange(start_date, end_date):
	for n in range(int ((end_date - start_date).days)):
		yield start_date + datetime.timedelta(n)


# nws_precip_1day_observed_shape_20140101.tar.gz

start_date = datetime.date(2014,1,1)
end_date = datetime.date(2014,2,1)
for single_date in daterange(start_date, end_date):
	print time.strftime("http://water.weather.gov/precip/p_download_new/%Y/%m/%d/new_precip_1day_observed_shape_%Y%m%d.tar.gz", single_date.timetuple())