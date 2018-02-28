# "Database code" for the DB Forum.

import datetime
import psycopg2


def get_posts():
    # Connect to DB
    db_conn = psycopg2.connect("dbname=forum")
    curr = db_conn.cursor()

    # run SELECT operation
    curr.execute("SELECT content, time from posts order by time desc;")

    # get data from query
    rows = curr.fetchall()

    # clean up DB connection
    curr.close()
    db_conn.close()

    return rows


def add_post(content):
    """Add a post to the 'database' with the current timestamp."""

    # Connect to DB
    db_conn = psycopg2.connect("dbname=forum")
    curr = db_conn.cursor()
    # run INSERT operation
    curr.execute("INSERT into posts(content, time) values(%s, %s);",
                 (content, datetime.datetime.now()))

    # clean up DB connection
    db_conn.commit()
    curr.close()
    db_conn.close()
