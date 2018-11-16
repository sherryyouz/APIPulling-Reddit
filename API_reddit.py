import urllib2
import requests
## Authentications. For Oauth use bearer instead of token
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}

## Retrieve the /r/python subreddit's top posts for the past day. 
# t for time and this is set to as string 'day'.
params = {"t": "day"}
# get the json response data
response1 = requests.get("https://oauth.reddit.com/r/python/top", headers=headers, params=params)
python_top = response1.json()
"""{'data': {'approved_by': None,
     'archived': False,
     'author': 'ingvij',
     ...
     'ups': 43,
     'url': 'http://hkupty.github.io/2016/Functional-Programming-Concepts-Idioms-and-Philosophy/',
     'user_reports': [],
     'visited': False},
     'kind': 't3'}"""
#Assign the list containing all the posts
python_top_articles = python_top["data"]["children"]
most_upvoted = ""
most_upvotes = 0
#Assign the ID for the post with the most upvotes to most_upvoted
for article in python_top_articles:
    ar = article["data"]
    if ar["ups"] >= most_upvotes:
        most_upvoted = ar["id"]
        most_upvotes = ar["ups"]

#Get all of the comments on the /r/python subreddit's to posts in the past day
response2 = requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u", headers=headers)
comments = response2.json()

"""{'data': {'approved_by': None,
      'archived': False,
      'author': 'larsga',
      ...
      'replies': {'data': {'after': None,
        'before': None,
        'children': [{'data': {'approved_by': None,
           'archived': False,
           'author': 'Deto',
           ...
           },
          ...
          ]
          }
          ...
          'url': 'https://www.reddit.com/r/Python/comments/4b6bew/using_pilpillow_with_mozjpeg/',
         'user_reports': [],
         'visited': False
         }"""

# Find the most upvoted comment. 
# Extract the comments list and assign the ID for the comment with the most upvotes.
comments_list = comments[1]["data"]["children"]
most_upvoted_comment = ""
most_upvotes_comment = 0
for comment in comments_list:
    co = comment["data"]
    if co["ups"] >= most_upvotes_comment:
        most_upvoted_comment = co["id"]
        most_upvotes_comment = co["ups"]
print(most_upvoted_comment)