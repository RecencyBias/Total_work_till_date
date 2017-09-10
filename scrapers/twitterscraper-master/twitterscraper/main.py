"""
This is a command line application that allows you to scrape twitter!
"""
import collections
import json
from argparse import ArgumentParser
from datetime import datetime
from os.path import isfile
from json import dump
import logging

from twitterscraper import query_tweets
from twitterscraper.query import query_all_tweets


class JSONEncoder(json.JSONEncoder):

    def default(self, obj):
        if hasattr(obj, '__json__'):
            return obj.__json__()
        elif isinstance(obj, collections.Iterable):
            return list(obj)
        elif isinstance(obj, datetime):
            return obj.isoformat()
        elif hasattr(obj, '__getitem__') and hasattr(obj, 'keys'):
            return dict(obj)
        elif hasattr(obj, '__dict__'):
            return {member: getattr(obj, member)
                    for member in dir(obj)
                    if not member.startswith('_') and
                    not hasattr(getattr(obj, member), '__call__')}

        return json.JSONEncoder.default(self, obj)


def main():
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
    try:
        parser = ArgumentParser(
            description=__doc__
        )

        parser.add_argument("query", type=str, help="Advanced twitter query")
        parser.add_argument("-o", "--output", type=str, default="tweets.json",
                            help="Path to a JSON file to store the gathered "
                                 "tweets to.")
        parser.add_argument("-l", "--limit", type=int, default=None,
                            help="Number of minimum tweets to gather.")
        parser.add_argument("-a", "--all", action='store_true',
                            help="Set this flag if you want to get all tweets "
                                 "in the history of twitter. This may take a "
                                 "while but also activates parallel tweet "
                                 "gathering. The number of tweets however, "
                                 "will be capped at around 100000 per 10 "
                                 "days.")
        args = parser.parse_args()

        if isfile(args.output):
            logging.error("Output file already exists! Aborting.")
            exit(-1)

        if args.all:
            tweets = query_all_tweets(args.query)
        else:
            tweets = query_tweets(args.query, args.limit)

        with open(args.output, "w") as output:
            dump(tweets, output, cls=JSONEncoder)
    except KeyboardInterrupt:
        logging.info("Program interrupted by user. Quitting...")
