from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
load_dotenv(os.path.join(BASE_DIR, '.env'))


# tweepy
def api_key():
    return {
        'consumer_key': os.getenv("CONSUMER_KEY"),
        'consumer_secret_key': os.getenv("CONSUMER_SECRET_KEY")
    }


# database
def db_query():
    return {
        'cr_tweet': os.getenv("CREATE_TABLE_TWEETS"),
        'cr_sentiment': os.getenv("CREATE_TABLE_SENTIMENT"),
        'ins_tweet': os.getenv("INSERT_TWEET"),
        'ins_sentiment': os.getenv("INSERT_SENTIMENT"),
        'up_sentiment': os.getenv("UPDATE_TABLE"),
        'null_sentiment': os.getenv("SELECT_NULL_SENTIMENT"),
        'by_date': os.getenv("SELECT_BY_DATE"),
        'date': os.getenv("SELECT_DATE"),
        'sentiment': os.getenv("SELECT_SENTIMENT")
    }
