# Twitter Frontend API

Get information using a front-end API that does not require a Twitter site login.

![Python 3.8](https://img.shields.io/badge/-Python%203.8-3776AB.svg?logo=python&style=plastic)
[![Release](https://img.shields.io/badge/-Release%200.1.3-00979D.svg?logo=release&style=plastic)](https://github.com/KohnoseLami/Twitter_Frontend_API/releases)

## Overview

Twitter runs, they force you to get a developer account to get information from Twitter. This is terrible. Your Twitter account could be suspended at any moment, or your application might not be approved at all. This is a module designed to work around them.
You can analyze the communication of Twitter's official site, generate a guest token, and get information from it.
It is not yet resistant to the retrieval of a large amount of information such as another page such as a search with detailed specification. You can retrieve only the information that appears the first time in the browser. Since the parameter analysis has not yet been completed, it is still in the process of development.

The document is not ready yet.

## Features

- You can obtain information such as:.
    * Generating Guest Tokens for Retrieving Information from Twitter
    * Obtain user details using a screen name or user ID
    * Retrieving a user's tweet using a screen name or user ID
    * Get Trend
    * Get results from search box (Search Candidates)
    * Get Search Results for Featured Tweets
    * Get Search Results for Latest Tweets
    * Get Image Tweet Search Results
    * Get Search Results for Video Tweets
    * Get user search results
    * Check if the screen name is available

## Install

Install with pip:

``pip install Twitter_Frontend_API``

To update:

``pip install Twitter_Frontend_API --upgrade``

Tested on Python 3.8.

## Usage

```python

from Twitter_Frontend_API import Client

api = Client()

print(api.generate_token())
print(api.user_info(screenname="Twitter")) #print(api.user_info(userid="783214"))
print(api.user_tweets(screenname="Twitter")) #print(api.user_tweets(userid="783214"))
print(api.trend())
print(api.searchbox("Text"))
print(api.topic_search("Text"))
print(api.latest_search("Text"))
print(api.image_search("Text"))
print(api.video_search("Text"))
print(api.user_search("Text"))
print(api.screenname_available("Screenname"))
```

## Donate

Bitcoin Address
16TCmq3QrAmuJied6KwNGuiqxuGpZDVVMp

## Legal
This is not official on Twitter. Use at your own risk.