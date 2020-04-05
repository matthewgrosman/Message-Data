# fb_stats.py
# This module collects all of the data from Facebook Messenger conversations


from collections import defaultdict
from datetime import datetime
import words


totals_data = defaultdict(int)
word_data = defaultdict(int)
dates_data = defaultdict(int)


def get_number_messages(message: dict) -> None:
    """ Updates the number of messages a person sent"""
    totals_data[message["sender_name"]] += 1


def get_number_words(message: str) -> None:
    """ Updates the number of keywords sent """
    for word in message.lower().split():
        if word in words.words:
            word_data[word] += 1


def get_dates(time: int) -> None:
    """ Updates the number of messages sent in a certain time """
    date_time = datetime.fromtimestamp(time/1000)
    formatted = date_time.strftime("%m") + "_" + date_time.strftime("%Y")

    dates_data[formatted] += 1


def convo_totals(conversation: dict) -> (dict, dict, dict):
    """ Call the functions to create the data dictionaries """
    for message in conversation["messages"]:
        get_number_messages(message)
        get_dates(message["timestamp_ms"])

        if "content" in message:
            get_number_words(message["content"])

    return totals_data, dates_data, words.sort_dict(word_data)
