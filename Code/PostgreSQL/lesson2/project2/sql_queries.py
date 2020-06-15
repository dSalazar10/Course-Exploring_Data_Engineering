# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays 
(
songplay_id serial PRIMARY KEY, 
timemstamp int NOT NULL, 
user_id int NOT NULL, 
level int NOT NULL,
song_id int NOT NULL, 
artist_id int NOT NULL, 
session_id int, 
location int, 
user_agent int
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users
(
user_id int PRIMARY KEY, 
first_name text NOT NULL, 
last_name text NOT NULL, 
gender boolean NOT NULL, 
level int NOT NULL
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs
(
song_id text PRIMARY KEY, 
title text NOT NULL, 
artist_id integer NOT NULL, 
year integer NOT NULL, 
duration integer NOT NULL
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists
(
artist_id integer PRIMARY KEY, 
name text NOT NULL, 
location text NOT NULL, 
longitude integer NOT NULL, 
latitude integer NOT NULL
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time
(
timestamp integer PRIMARY KEY, 
hour integer NOT NULL, 
day integer NOT NULL, 
week integer NOT NULL, 
month integer NOT NULL, 
year integer NOT NULL, 
weekday integer NOT NULL
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays
(
songplay_id, 
timestamp, 
user_id, 
level, 
song_id, 
artist_id, 
session_id, 
location, 
user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users
(
user_id, 
first_name, 
last_name, 
gender, 
level) 
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT(user_id) DO UPDATE SET level = excluded.level
""")

song_table_insert = ("""
INSERT INTO songs
(
song_id, 
title, 
artist_id, 
year, 
duration) 
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT(song_id) DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO artists
(
artist_id, 
name, 
location, 
longitude, 
latitude) 
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT(artist_id) DO NOTHING
""")


time_table_insert = ("""
INSERT INTO time
(
timestamp, 
hour, day, 
week, 
month, 
year, 
weekday) 
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT(timestamp) DO NOTHING
""")

# FIND SONGS

# Implement the song_select query in sql_queries.py to find the song ID and artist ID based on the title, artist name, and duration of a song.
# Select the timestamp, user ID, level, song ID, artist ID, session ID, location, and user agent and set to songplay_data
song_select = ("""
SELECT timestamp, userId, level, song_id, artist_id, artist_location, session_id, user_agent FROM \
                        ((user JOIN songplay ON user.user_id=songplay.user_id) JOIN \
                        song ON song.song_id=songplay.song_id) JOIN \
                        artist ON artist.artist_id=songplay.artist_id
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]