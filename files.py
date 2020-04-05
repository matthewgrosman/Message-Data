# files.py
# This module handles the opening of files, which have been pre-formatted and
# set up in a folder already


import json


def get_facebook() -> (dict, str):
    """ Returns a dictionary with a Facebook Messenger conversation """
    name = input("Enter name: ").lower()
    filename = f'C:\\message_data\\{name}\\{name}_fb.json'

    try:
        with open(filename, "r") as f:
            return json.load(f), name

    except FileNotFoundError:
        print("File not found!")
        return {"messages": []}, name
