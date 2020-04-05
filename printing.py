# printing.py
# This module prints certain top stats


def print_stats(stats: dict, totals: dict, dates: dict) -> None:
    """ Takes stats and prints them in a certain format """
    print()

    for person, total in totals.items():
        print(f'{person} sent {total} messages.')

    print()

    for key, value in stats.items():
        print(f'{key} : {value}')

    print()

    for date, amount in dates.items():
        print(f'{amount} messages were sent during {date}.')
