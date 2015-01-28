update precipitation set timestamp = to_timestamp(date, 'YYYYMMDD');
drop table total_macrowatershed_precipitation;
create table total_macrowatershed_precipitation as select sum(globvalue) as total_precipitation, timestamp from precipitation group by timestamp order by timestamp;


create table total_macrowatershed_precipitation_stats as select sum(globvalue) as total_precipitation, count(globvalue) as num_points, timestamp from precipitation group by timestamp order by timestamp;

create table total_macrowatershed_precipitation_stats_2 as select count(globvalue) as num_points, timestamp from precipitation where globvalue > .2 group by timestamp order by timestamp;


# this one does’t make a lot of sense.
select *, stat1.total_precipitation / stat2.num_points from total_macrowatershed_precipitation_stats_2 stat2 join total_macrowatershed_precipitation_stats stat1 on stat2.timestamp = stat1.timestamp where total_precipitation > 500;

select *, total_precipitation / num_points from total_macrowatershed_precipitation_stats where total_precipitation > 100;


create table fifth_order_watersheds_totals
as select fifthorderwatersheds.gid, timestamp, sum(globvalue) from fifthorderwatersheds, precipitation
where ST_WITHIN(precipitation.geom, fifthorderwatersheds.geom)
and fifthorderwatersheds.shape_area > .1
group by fifthorderwatersheds.gid, timestamp;

create table metabasin_totals
as select metabasinpolygons.gid, metabasinpolygons.name, timestamp, sum(globvalue) from metabasinpolygons, precipitation
where ST_WITHIN(precipitation.geom, metabasinpolygons.geom)
group by metabasinpolygons.gid, metabasinpolygons.name, timestamp;

alter table metabasin_totals add column month integer;
update metabasin_totals set month = to_number(to_char(timestamp, 'MM'), '99');

