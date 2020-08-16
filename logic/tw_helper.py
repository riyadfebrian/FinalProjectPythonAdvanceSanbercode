import string

from .credential import api_key
import nltk
import tweepy
import re
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import pandas as pd

# Stemmer Object
from .dt_helper import dayBefore

factory = StemmerFactory()
stemmer = factory.create_stemmer()

# Configure Stopwords
stop_words = set(stopwords.words('indonesian'))

key = api_key()
auth = tweepy.OAuthHandler(key['consumer_key'],
                           key['consumer_secret_key'])
api = tweepy.API(auth)


def clean_tweets(tweet):
    # 1. Case Folding
    tweet = re.sub("@[A-Za-z0-9]", "", tweet)  # remove tag username
    tweet = re.sub(r"http\S+", "", tweet)  # Remove url
    tweet = re.sub(r"\d+", "", tweet)  # Remove Numbers
    tweet = tweet.lower().strip()  # remove trailing spaces & lowerize
    tweet = tweet.replace('\n\n', '')  # Remove tweet line break

    # 2. Stemming
    tweet = stemmer.stem(tweet)

    # 3. Punctuation
    tweet = tweet.translate(str.maketrans("", "", string.punctuation))

    # 4. Tokenization
    tokens = nltk.tokenize.word_tokenize(tweet)

    # 5. Remove Stop Words
    tweet = [w for w in tokens if not w in stop_words]

    return " ".join(tweet)


def scrape_topic(search_words: str = 'vaksin covid',
                 count: int = 0,
                 max_tweet: int = 1000):
    new_search = search_words + " -filter:retweets"

    date_since = dayBefore(count)

    tweets = tweepy.Cursor(api.search,
                           q=new_search,
                           lang="in",
                           tweet_mode='extended',
                           since=date_since).items(max_tweet)
    items = []
    for tweet in tweets:
        items.append([tweet.id,
                      tweet.created_at.date().isoformat(),
                      tweet.user.screen_name,
                      clean_tweets(tweet.full_text)])

    hasil = pd.DataFrame(items, columns=['tweet_id', 'date', 'user', 'tweet'])

    return hasil


def sentiment_analysis(df):
    with open("dataset/kata_positif.txt", "r") as pos_list:
        pos_kata = pos_list.readlines()

    with open("dataset/kata_negatif.txt", "r") as neg_list:
        neg_kata = neg_list.readlines()

    result = []
    for item in df.tweet.values:
        count_p = 0
        count_n = 0

        for kata_pos in pos_kata:
            if kata_pos.strip() in item:
                count_p += 1

        for kata_neg in neg_kata:
            if kata_neg.strip() in item:
                count_n += 1

        result.append(count_p - count_n)

    df['value'] = result
    return df
