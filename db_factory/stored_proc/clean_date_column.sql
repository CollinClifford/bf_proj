alter table reports 
add column date varchar(50)

update reports 
set date = (
	case  
		when day is not null and month_number is not null then concat(month_number, '/', day, '/', year)
		else null
	end
);