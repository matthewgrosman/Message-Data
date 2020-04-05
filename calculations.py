# calculations.py
# This module performs calculations on data to get statistics


statistics = {
    "high_month": "",
    "low_month": "",
    "total_messages": 0,
    "ratio": 0,
    "pct_change": 0,
    "high_word": ""
}


def get_dates_statistics(d: dict) -> None:
    """ Gathers statistics pertaining to the dates data """
    sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)

    statistics["high_month"] = sorted_d[0][0]
    statistics["low_month"] = sorted_d[len(sorted_d)-1][0]

    if len(d) > 1:
        months = list(d.values())
        statistics["pct_change"] = (months[0]/months[1])*100


def get_totals_statistics(d: dict) -> None:
    """ Gathers statistics pertaining to the totals data """
    for amount in d.values():
        statistics["total_messages"] += amount

    sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    statistics["ratio"] = sorted_d[0][1] / sorted_d[1][1]


def get_words_statisitcs(d: dict) -> None:
    """ Gathers statistics pertaining to the words data """
    statistics["high_word"] = list(d.keys())[0]


def get_statistics(totals: dict, words: dict, dates: dict) -> dict:
    """ Gathers statistics pertaining to the given data """
    get_dates_statistics(dates)
    get_words_statisitcs(words)
    get_totals_statistics(totals)

    return statistics
