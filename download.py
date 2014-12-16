#!/usr/bin/python
import datetime
import time
import wget
from osgeo import ogr
import datetime
import tarfile

def daterange(start_date, end_date):
	for n in range(int ((end_date - start_date).days)):
		yield start_date + datetime.timedelta(n)


# nws_precip_1day_observed_shape_20140101.tar.gz

start_date = datetime.date(2012,1,1)
end_date = datetime.date(2013,1,1)
for single_date in daterange(start_date, end_date):
	download_url = time.strftime("http://water.weather.gov/precip/p_download_new/%Y/%m/%d/nws_precip_1day_observed_shape_%Y%m%d.tar.gz", single_date.timetuple())
	print download_url
	wget.download(download_url, 'downloads_2011')

	filename = time.strftime("nws_precip_1day_observed_shape_%Y%m%d.tar.gz", single_date.timetuple())
	path = "downloads_2012/"+filename

	tar = tarfile.open(path)
	tar.extractall('shapes_2012')
	tar.close()

	filename = time.strftime("nws_precip_1day_observed_%Y%m%d.shp", single_date.timetuple())
	path = "shapes_2012/"+filename

	# and append the date of the file to the shapes
	driver = ogr.GetDriverByName('ESRI Shapefile')
	print path
	dataSource = driver.Open(path, 1) #1 is read/write

	#define floating point field named DistFld and 16-character string field named Name:
	fldDef = ogr.FieldDefn('Date', ogr.OFTString)
	fldDef.SetWidth(10) #16 char string width

	#get layer and add the 2 fields:
	layer = dataSource.GetLayer()
	layer.CreateField(fldDef)
	for feat in layer:
		datestring = time.strftime("%Y%m%d", single_date.timetuple())
		feat.SetField('Date',datestring) 
		layer.SetFeature(feat)
	dataSource = None


