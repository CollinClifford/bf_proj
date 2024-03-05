def create_reports_ll_vw(cursor):
    create_query = """
    create view reports_ll_vw as
        select r.report_number
            , ll.county
            , ll.state
            , ll.latitude
            , ll.longitude
        from reports r 
        left join lat_long ll 
            on r.county = ll.county
            and r.state = ll.state
        order by r.county;
    """

    cursor.execute(create_query)