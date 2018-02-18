import sys
from config import get_client
from birdy.twitter import UserClient


# You can change where the state files are kept, if you want
STATE_DIR = 'state/'

def get_last_seen_tweet_id(client, username, filepath):
    # open & read target user state file
    try:
        with open(filepath, "r") as myfile:
            last_seen_tweet_id = myfile.read().strip()
    except:
        # no state file exists. let's initialize one
        response = client.api.statuses.user_timeline.get(screen_name=str(username),count=1,trim_user=1)
        # if we received a response, write that ID to the state file
        if len(response.data) > 0:
            last_seen_tweet_id = int(response.data[0].id)
            update_last_seen_tweet_id(filepath, last_seen_tweet_id)
        exit()
    return last_seen_tweet_id

def update_last_seen_tweet_id(filepath, tweet_id):
    # update the last tweet we've seen
    with open(filepath, "w") as myfile:
        myfile.write(str(tweet_id))


def main(argv):

    # Make sure we received a target user
    if len(argv) != 2:
        print "usage: python sycophant.py username"
        sys.exit()

    TARGET_USER = argv[1]
    LAST_TWEET = TARGET_USER + "_last_tweet"

    # create twitter client
    client = get_client()

    # create twitter wrapper
    twitter = Twitter(client)

    # open & read target user state file
    last_id = get_last_seen_tweet_id(client, TARGET_USER, STATE_DIR + LAST_TWEET)

    # Get the user's timeline since the tweet in the target state file
    response = client.api.statuses.user_timeline.get(screen_name=str(TARGET_USER),since_id=str(last_id),exclude_replies='true')

    if len(response.data) > 0:

        last_id = int(response.data[0].id)

        if not response.data[0].favorited:
            twitter.favorite(last_id)

        if not response.data[0].retweeted:
            twitter.retweet(last_id)

        # update the last tweet we've seen
        update_last_seen_tweet_id(STATE_DIR + LAST_TWEET, last_id)


if __name__ == "__main__":
    main(sys.argv)
