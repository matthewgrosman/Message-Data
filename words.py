# words.py
# This module specifies what keywords to look for, as well as contains
# functions that sort and condense the word data collected


words = ["nayoung", "mattyg", "derek", "steven", "sgeven", "fuck", "fuxk", "bitch", "shit",
         "badass", "gay", "uci", "ucla", "snake", "fake", "dick", "khoi", "jordan", "sorry",
         "racist", "woo", "friend", "boba", "moorpark", "irvine", "sad", "cry", "depressed",
         "depression", "bree", "lmao", "lol", "haha", "damn", "dang", "nikhita",
         "mood", "asshole", "jalen", "jennifer", "duck", "die", "qixuan", "fml", "lonely",
         "leo", "cancel", "ltg", "overwatch", "zombies", "munchie", "drunk", "high", "messenger",
         "facebook", "vlog", "hahahahaha", "hahahaha", "hahaha", "bruh", "hahhaha", "hahahahahaha",
         "hahahahahahahahahahahaha","hahahahahahaha", "hahahahahahahaha", "bro", "bf", "china",
         "lmaoo", "lmaooo", "lolol", "lmaoooo", "love", "daniel", "music", "frank", "sushi", "taco",
         "tacos", "ramen", "kbbq", "happy", "abbi", "math", "bernie", "yang", "cameo", "freestyle",
         "roast", "cried", "crying", "mattg"]

variations = {
    "haha": ["hahahahaha", "hahahaha", "hahaha", "hahhaha", "hahahahahaha",
             "hahahahahahahahahahahaha", "hahahahahahaha", "hahahahahahahaha"],
    "steven": ["sgeven"],
    "lmao": ["lmaoo", "lmaooo", "lmaoooo"],
    "lol": ["lolol"],
    "fuck": ["fuxk", "duck"],
    "taco": ["tacos"],
    "depressed": ["depression"],
    "cry": ["cried", "crying"],
    "mattyg": ["mattg"]
}


def condense_dict(d: dict) -> dict:
    """ Removes duplicate words or words with 0 entries """
    for original, variation in variations.items():
        for word in variation:
            d[original] += d[word]
            del d[word]

        if d[original] == 0:
            del d[original]

    return d


def sort_dict(d: dict) -> dict:
    """ First condenses and then sorts the dictionary by decreasing value """
    condense_dict(d)

    return {k: v for k,v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
