# Database code for the DB news

import datetime
import psycopg2

DBNAME = "news"


def get_query_results(query):
    """Return query results from the database"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    query_results = c.fetchall()
    db.close()
    return query_results


def main(query):
    return get_query_results(query)


if __name__ == '__main__':
    main()
