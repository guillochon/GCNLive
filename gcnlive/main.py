import os

import twitter


def main():
    key_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), '.keysecret')
    with open(key_path, 'r') as f:
        keys = f.read().splitlines()
    api = twitter.Api(consumer_key=keys[0],
                      consumer_secret=keys[1],
                      access_token_key=keys[2],
                      access_token_secret=keys[3])
    api.PostUpdate('My first tweet!')
