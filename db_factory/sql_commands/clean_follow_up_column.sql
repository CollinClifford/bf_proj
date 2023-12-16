update reports 
set follow_up =
(
	case
		when follow_up like 'Follow-up investigation report by BFRO Investigator %' then SUBSTRING(follow_up, 53)
		else null
	end
);

update reports
set follow_up = (
case 
	when follow_up like '%:' then substring(follow_up FROM 1 FOR length(follow_up) - 1)
	else follow_up
end
)