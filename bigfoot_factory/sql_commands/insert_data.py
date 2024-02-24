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

def insert_location_data(cursor, data):
    # Define the columns manually based on the expected order of values
    columns = ['county', 'state', 'latitude', 'longitude']
    
    # Extract values from the 'data' list
    values = data

    # Builds insert query
    insert_query = f"""
        INSERT INTO lat_long (county, state, latitude, longitude)
        VALUES ({', '.join(['%s' for _ in range(len(columns))])});
        """
    # inserts data 
    cursor.execute(insert_query, values)
