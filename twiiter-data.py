import io
import sys
from textblob import TextBlob
import tweepy
import re


consumer_key = 'WZYYKkpJldJW6ghIvBPkETQ38'
consumer_secret = '8iQGV8kr2y6KxtSzkqFmq7iXjq8urTwiQWqhsxo8O91gnUD7kV'

access_token = '1190363683475484672-K7wQivvnCSSPdimp0gb4uH9Mv2mvNk'
access_token_secret = 'XUXDBsU8gF5LhIiUAPfrpdPjEN9CFZdGQFdJNqwpX7f10'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Step2 - Call the API
api = tweepy.API(auth)
output = ''

with io.open("Fracking-Sarcasm-using-Neural-Network.txt") as fopen:
    file_content = fopen.read().splitlines()

for i in range(0, len(file_content)-1):
    try:
        temp = re.split(r'\t+', file_content[i])
        tweet, label = temp[0], temp[1]
        status = api.get_status(tweet)
        output += status.text + " " + label + "\n"
    except:
        continue
outputfile = io.open('tweetcontent.txt', 'w', encoding='utf8')
outputfile.write(output)
outputfile.close()
