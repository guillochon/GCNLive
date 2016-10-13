import os
import sys
import voeventparse
import twitter
import voeventparse

def tweet(text, key_path):
    with open(key_path, 'r') as f:
        keys = f.read().splitlines()
    api = twitter.Api(consumer_key=keys[0],
                      consumer_secret=keys[1],
                      access_token_key=keys[2],
                      access_token_secret=keys[3])

    api.PostUpdate(text)

def main():
    key_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), '.keysecret')
    stdin = sys.stdin.read()
    v = voeventparse.loads(stdin)
    response = process_voevent(v)
    if response is not None:
        print(response)
        # tweet(response, key_path)




def handle_grb(v):
    coords = voeventparse.pull_astro_coords(v)
    text = "Swift GRB Alert received, coords are {}".format(coords)
    return text

def handle_pointing(v):
    coords = voeventparse.pull_astro_coords(v)
    text = "Swift repointing, coords are {}".format(coords)
    return text

prefix_handler_map = {
    'ivo://nasa.gsfc.gcn/SWIFT#BAT_GRB_Pos': handle_grb,
    "ivo://nasa.gsfc.gcn/SWIFT#Point_Dir_": handle_pointing,
}

def process_voevent(v):
    ivorn = v.attrib['ivorn']
    for prefix, handler in prefix_handler_map.items():
        if ivorn.startswith(prefix):
            return handler(v)
    return None