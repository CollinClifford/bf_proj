alter table reports
add column month_number int

update reports
set month_number =
(
case
	when month = 'January' then 1
	when month = 'February' then 2
	when month = 'March' then 3
	when month = 'April' then 4
	when month = 'May' then 5
	when month = 'June' then 6
	when month = 'July' then 7
	when month = 'August' then 8
	when month = 'September' then 9
	when month = 'October' then 10
	when month = 'November' then 11
	when month = 'December' then 12
	else null
end
)
