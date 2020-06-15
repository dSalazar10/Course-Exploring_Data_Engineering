import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    - Creates and connects to the sparkifydb
    - Returns the connection and cursor to sparkifydb
    """
    # connect to default database
    try:
        conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    except psycopg2.Error as e: 
        print("Error: Could not make connection to the Postgres database")
        print(e)
    try:
        cur = conn.cursor()
    except psycopg2.Error as e: 
        print("Error: Could not get curser to the Database")
        print(e)
    conn.set_session(autocommit=True)    
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkdb")
    cur.execute("CREATE DATABASE sparkdb WITH ENCODING 'utf8' TEMPLATE template0")
    # close connection to default database
    conn.close()    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkdb user=student password=student")
    cur = conn.cursor()
    return cur, conn

def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except Exception as e:
            print("Error: Issue dropping table")
            print(e)


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except Exception as e:
            print("Error: Issue creating table")
            print(e)


def main():
    """
    - Drops (if exists) and Creates the sparkify database. 
    
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    cur, conn = create_database()
    create_tables(cur, conn)
    drop_tables(cur, conn)
    conn.close()


if __name__ == "__main__":
    main()