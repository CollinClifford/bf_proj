def insert_data(cursor, data):

    # Finds the key and values for insertion
    columns = data.keys()
    values = [data[column] for column in columns]

    # Builds insert query
    insert_query = f"""
        INSERT INTO reports ({', '.join(columns)})
        VALUES ({', '.join(['%s' for _ in range(len(columns))])});
        """
    
    # inserts data 
    cursor.execute(insert_query, values)
