# reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.
import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *
import json
from datetime import datetime
import numpy as np


def process_song_file(cur, filepath):
    """
    This procedure processes a song file whose filepath has been provided as an arugment.
    It extracts the song information in order to store it into the songs table.
    Then it extracts the artist information in order to store it into the artists table.

    INPUTS: 
    * cur the cursor variable
    * filepath the file path to the song file
    """
    # open song file
    df = pd.DataFrame(json.load(open(filepath)), index=[0])

    # insert song record
    song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']]
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    This procedure processes a log file whose filepath has been provided as an arugment.
    It extracts the log information in order to store it into the time table.
    Then it extracts the user information in order to store it into the users table.

    INPUTS: 
    * cur the cursor variable
    * filepath the file path to the log file
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df['page']=='NextSong'

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms')
    
    # insert time data records
    time_data = pd.Series([t.astype(np.int64), t.dt.hour, t.dt.day, t.dt.week, t.dt.month, t.dt.year])
    column_labels = ('timestamp', 'hour', 'day', 'week', 'month', 'year', 'weekday')
    time_df = pd.DataFrame(dict(zip(column_labels, time_data)))

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row['timestamp'], row['userId'], row['level'], row['song_id'], artistid, row['artist_location'], row['session_id'], row['user_agent'])
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    This procedure gets all the files matching extension from directory,
    iterate over files, and performs the input function on each file

    INPUTS: 
    * cur the cursor variable
    * conn the connection variable
    * filepath the directory where the data files exist
    * func the callback function
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """
    This is the driver code. It creates a connection to the database,
    processes the song data, processes the log data, and closes the
    database
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()