def create_table(cursor):

    # Declares the table columns.  In future releases, it'd be great to make this dynamic
    create_table_query = """
    CREATE TABLE IF NOT EXISTS reports (
        report_number TEXT,
        report_classification TEXT,
        submitted_by TEXT,
        summary TEXT,
        year TEXT,
        season TEXT,
        month TEXT,
        date TEXT,
        state TEXT,
        county TEXT,
        location_details TEXT,
        nearest_town TEXT,
        nearest_road TEXT,
        observed TEXT,
        also_noticed TEXT,
        other_witnesses TEXT,
        environment TEXT,
        other_stories TEXT,
        time_and_conditions TEXT,
        follow_up TEXT,
        follow_up_details TEXT
    );
    """

    # Creates table
    cursor.execute(create_table_query)