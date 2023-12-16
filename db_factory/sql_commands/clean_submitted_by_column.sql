--------------------------------
--Cleaning Submitted by column--
--------------------------------
update
  reports
set
  submitted_by = case
    when submitted_by like 'Submitted  %' then substring(submitted_by, 10)
    else submitted_by
  end;

update
  reports
set
  submitted_by = case
    when submitted_by like '% by %' then substring(submitted_by, 6)
    else submitted_by
  end;

update
  reports
set
  submitted_by = case
    when submitted_by like '% witness %' then substring(submitted_by, 10)
    else submitted_by
  end;

alter table
  reports
add
  column submitted_by_date varchar(255);

update
  reports
set
  submitted_by = substring(
    submitted_by,
    1,
    position(' on ' in submitted_by) - 1
  ),
  submitted_by_date = substring(
    submitted_by,
    position(' on ' in submitted_by) + 4
  )
where
  submitted_by like '% on %';

update
  reports
set
  submitted_by_date = substring(
    submitted_by_date,
    CHARINDEX(', ', submitted_by_date) + 2,
    LEN(submitted_by_date)
  );

update
  reports
set
  submitted_by_date = to_char(
    to_date(
      trim(
        both ' .'
        from
          trim(split_part(submitted_by_date, ',', 2)) || trim(split_part(submitted_by_date, ',', 3)),
          'Month DD YYYY'
      ),
      'MM/DD/YYYY'
    )
    where
      submitted_by_date like '%,%';

update
  reports
set
  submitted_by_date = (
    case
      when submitted_by_date like '%January%' then REPLACE(submitted_by_date, 'January', '01')
      when submitted_by_date like '%February%' then replace(submitted_by_date, 'February', '02')
      when submitted_by_date like '%March%' then REPLACE(submitted_by_date, 'March', '03')
      when submitted_by_date like '%April%' then replace(submitted_by_date, 'April', '04')
      when submitted_by_date like '%May%' then REPLACE(submitted_by_date, 'May', '05')
      when submitted_by_date like '%June%' then replace(submitted_by_date, 'June', '06')
      when submitted_by_date like '%July%' then REPLACE(submitted_by_date, 'July', '07')
      when submitted_by_date like '%August%' then replace(submitted_by_date, 'August', '08')
      when submitted_by_date like '%September%' then REPLACE(submitted_by_date, 'September', '09')
      when submitted_by_date like '%October%' then replace(submitted_by_date, 'October', '10')
      when submitted_by_date like '%November%' then REPLACE(submitted_by_date, 'November', '11')
      when submitted_by_date like '%December%' then replace(submitted_by_date, 'December', '12')
    end
  );

update
  reports
set
  submitted_by_date = trim(
    '/'
    from
      regexp_replace(submitted_by_date, '[^0-9]', '/', 'g')
  );