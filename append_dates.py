#!/usr/bin/python
from osgeo import ogr
import datetime
import time

def daterange(start_date, end_date):
	for n in range(int ((end_date - start_date).days)):
		yield start_date + datetime.timedelta(n)

#20130602.
start_date = datetime.date(2009,1,1)
end_date = datetime.date(2011,7,31)
for single_date in daterange(start_date, end_date):
	driver = ogr.GetDriverByName('ESRI Shapefile')
	filename = time.strftime("nws_precip_1day_observed_%Y%m%d.shp", single_date.timetuple())
	path = "shapes_2013/"+filename
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


