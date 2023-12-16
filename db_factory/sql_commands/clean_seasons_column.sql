--------------------------
--cleaning season column--
--------------------------
update reports
set season = null 
where season not in (
'Fall',
'Spring',
'Winter',
'Summer'
);