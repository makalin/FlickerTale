import markovify
import tweepy
import time
from secrets import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET  # Store these securely!

# Sample corpus for story generation (replace with your own text file later)
CORPUS = """
The shadow crept along the wall. Stars blinked out one by one. She whispered to the void. 
A clock ticked in reverse. The cat stared with human eyes. Dust settled on forgotten dreams.
"""

# Build Markov model
text_model = markovify.Text(CORPUS, state_size=2)

# Twitter API setup
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

def generate_story(max_chars=280):
    while True:
        story = text_model.make_short_sentence(max_chars)
        if story and len(story) <= max_chars:
            return story

def post_story():
    story = generate_story()
    try:
        api.create_tweet(text=story)
        print(f"Posted: {story}")
    except Exception as e:
        print(f"Error posting: {e}")

# Run every 4 hours (adjust as needed)
if __name__ == "__main__":
    while True:
        post_story()
        time.sleep(4 * 60 * 60)  # 4 hours in seconds