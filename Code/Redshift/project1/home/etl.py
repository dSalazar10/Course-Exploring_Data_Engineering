import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    Amazon recommends the following steps for loading data from S3:
    1. Split your data into multiple files
    - This has been done for us already
    - Amazon recommneds that we make the count of files match the modulus of
    the number of slices in our cluster. In this case we are using a dc1.large
    cluster, which has 2 slices per node, and we will use 4 nodes, for a total
    of 8 slices. The song data set contains roughly 17,000 files and the logs
    data set contains 30 files. This will allow us to split the song data into
    2,125 per slice and the log data into roughly 4 files per slice.
    2. Upload your files into Amazon S3
    - This has been done for us already
    - You can view the song data here: 
        * https://s3.console.aws.amazon.com/s3/buckets/udacity-dend/song_data
    - You can view the log data here: 
        * https://s3.console.aws.amazon.com/s3/buckets/udacity-dend/log_data
    - This will use the following links to load the data: 
        * Song data: s3://udacity-dend/song_data
        * Log data: s3://udacity-dend/log_data
    3. Run a COPY command to load the table
    - This function accomplishes this taks
    4. Verify that the data was loaded correctly
    - This is ignored for now

    INPUTS: 
    * cur the cursor variable
    * filepath the file path to the song file
    """
    # copy_table_queries = [staging_events_copy, staging_songs_copy]
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    This proceedure inserts data from the staged tables into the 
    proper tables in Redshift
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    This is the driver code. It configures the enviroonment variables using the config file,
    creates a connection to the Redshift database, loads the staged data, inserts the staged data
    into the proper tables, then closes the connection
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
        load_staging_tables(cur, conn)
    except Exception as e:
        print("Unable to load staging table.")
        print(e)
    
    try:
        insert_tables(cur, conn)
    except Exception as e:
        print("Unable to insert table.")
        print(e)

    try:
        conn.close()
    except Exception as e:
        print("Unable to close connection.")
        print(e)

if __name__ == "__main__":
    main()