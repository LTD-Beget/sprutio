import random


def random_hash():
    hash_str = random.getrandbits(128)
    return "%032x" % hash_str
