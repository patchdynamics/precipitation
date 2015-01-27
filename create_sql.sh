#!/bin/bash
rm sql/data.sql
find shapes/*.shp -exec shp2pgsql -a {} precipitation > sql/data.sql \;
