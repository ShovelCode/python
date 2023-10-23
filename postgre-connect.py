
import psycopg2
from psycopg2 import sql

try:
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        host="your_host",
        database="your_database",
        user="your_user",
        password="your_password",
        port="your_port"
    )

    # Create a cursor object
    cur = conn.cursor()

    # SQL query to update a row where id = 1
    update_query = sql.SQL(
        "UPDATE users SET name = %s, email = %s WHERE id = %s"
    )

    # Data to be updated
    new_name = "Updated_Name"
    new_email = "updated_email@example.com"
    target_id = 1

    # Execute the SQL query
    cur.execute(update_query, (new_name, new_email, target_id))

    # Commit changes
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()

except Exception as e:
    print(f"An error occurred: {e}")

```

