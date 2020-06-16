import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Configures the Python-sql environment variables using the config file
    
    - Establishes connection with the Redshift database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    try:
        conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
        cur = conn.cursor()
    except Exception as e:
        print("Unable to connect to Redshift.")
        print(e)
    try:
        cur = conn.cursor()
    except Exception as e:
        print("Unable to get cursor.")
        print(e)

    try:
        drop_tables(cur, conn)
    except Exception as e:
        print("Unable to drop table.")
        print(e)
    
    try:
        create_tables(cur, conn)
    except Exception as e:
        print("Unable to create table.")
        print(e)
    
    try:
        conn.close()
    except Exception as e:
        print("Unable to close connection.")
        print(e)
    


if __name__ == "__main__":
    main()