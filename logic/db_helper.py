import sqlite3
from datetime import datetime
from logic.credential import db_query
from logic.dt_helper import minus_one, convert_from_str
import pandas as pd

_query = db_query()


def connect():
    return sqlite3.connect(r'db/database.db')


def execute(query: str,
            value: list = [],
            single: bool = True):
    conn = connect()
    with conn:
        if single:
            conn.execute(query)
        else:
            conn.executemany(query, value)
        conn.commit()


def init():
    """Initialization for creating database schema"""
    execute(query=_query['cr_tweet'])
    execute(query=_query['cr_sentiment'])


def insert_tweet(value):
    """Insert Multiple Tweets and initial Sentiment"""
    execute(query=_query['ins_tweet'],
            value=value,
            single=False)

    id_value = [[element[0]]for element in value]

    execute(query=_query['ins_sentiment'],
            value=id_value,  # Tweet ID value
            single=False
            )


def update_sentiment(value):
    """Updating sentiment analysis value"""
    execute(query=_query['up_sentiment'],
            value=value,  # Value consist of sentiment value and tweet ID
            single=False)


def get_date():
    """Get Date Params from database"""
    temp = pd.read_sql_query(_query['date'], connect())
    return temp.values


def get_records_date(start_date, end_date):
    """Get records from range date"""
    start = minus_one(start_date)
    temp = pd.read_sql_query(_query['by_date'],
                             connect(),
                             params=[start, end_date])
    return temp


def get_sentiment(start_date, end_date):
    start = minus_one(start_date)
    temp = pd.read_sql_query(_query['sentiment'],
                             connect(),
                             params=[start, end_date])
    return temp


def get_null_sentiment():
    temp = pd.read_sql_query(_query['null_sentiment'], connect())
    return temp



if __name__ == '__main__':
    # create_table(_query['cr_tweet'])
    # create_table(_query['cr_sentiment'])

    # ins_upd_table(_query['ins_tweet'], [(5000, '2020-08-21', 'riyadfebrian', 'ajsdfsdfsdf'),
    #                                   (7000, '2020-08-22', 'bakemono', 'llppplplplpl')])

    # ins_upd_table(_query['ins_sentiment'], [(1112,), (10000,)])

    # insert_table(_query['up_sentiment'], [(60, 1244)])

    # a = pd.read_sql_query(_query['null_sentiment'], connect())

    a = get_sentiment('2020-08-10', '2020-08-21')
    print(a)
    print(len(a.value.unique()))

    print('Berhasil')
