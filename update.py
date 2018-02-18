import sys
from config import get_client
from birdy.twitter import UserClient
from twitter import Twitter

def main(argv):

    # Make sure we received target tweet text
    if len(argv) != 2:
        print "usage: python update.py 'status update text'"
        sys.exit()

    UPDATE_TEXT = argv[1]

    # create twitter client
    client = get_client()

    # create Twitter...
    twitter = Twitter(client)

    # post an update
    twitter.update(UPDATE_TEXT)


if __name__ == "__main__":
    main(sys.argv)