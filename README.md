# 2023-02-03 Addendum
This module is currently not maintained and the person who requested the pull has now quit parsing Twitter.
I do Twitter self-bots for work, and I won't write about any further improvements or private APIs for mobile.

If I were to leave some useful information here, the Twitter API v 1.1 endpoints would still all work as usual using the "auth_token" in the account credentials cookie and the TweetDeck Authorization token.
(Bearer AAAAAAAAAAAAAAAAAAAAAF7aAAAAAAAASCiRjWvh7R5wxaKkFp7MM%2BhYBqM%3DbQ0JPmjU9F6ZoMhDfI4uTNAaQuTDm2uO9x3WFVr2xBZ2nhjdP0)

The previous login program included in this module can be used to get the "auth _ token," but now logins using task.json are used.
(Tip: The login API is the same for mobile and site (Why? LOL))
(API Keys: https://gist.github.com/shobotch/5160017)

It also now says it's mainly GraphQL, not v 1.1, but the mobile version still uses the v2 API, the GraphQL API, the v 1.1 API and, to top it off, v 1.
For a while you will be able to run v 1.1 just by changing the Authorization key.

Also, there is now automated detection, so if you do a self-bot recklessly, your account will be immediately suspended.
(Hint: Twitter barely detects in user agents, anywhere else)

Automating with easy knowledge and gathered information is a high risk.
Also, freezing is done per IP. Remember that if you automate and your account is suspended, the account of the family member you live with carries the risk of account suspension as well.

Automating Twitter is currently easier than social networks like Instagram and Facebook, but with hidden risks.

# Twitter Frontend API
Get information using a front-end API that does not require a Twitter site login.

![Python 3.9](https://img.shields.io/badge/-Python%203.9-3776AB.svg?logo=python&style=plastic)
[![Release](https://img.shields.io/badge/-Release%201.1.1-00979D.svg?logo=release&style=plastic)](https://github.com/KohnoseLami/Twitter_Frontend_API/releases)

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

Tested on Python 3.9.0

## Usage

```python

from Twitter_Frontend_API import Client

api = Client()

# SetUp
print(api.generate_ct0())
print(api.generate_authenticity())
print(api.generate_token())

# Twitter API v1.1
print(api.rate_limit_status())
print(api.collections_entries("custom-539487832448843776"))
print(api.favorites_list("_SNQ"))
print(api.followers_ids("_SNQ"))
print(api.followers_list("_SNQ"))
print(api.friends_ids("_SNQ"))
print(api.friends_list("_SNQ"))
print(api.friendships_show("_SNQ", "Shadow_Ban_Bot"))
print(api.geo_id("06ef846bfc783874"))
print(api.geo_reverse_geocode("35.79449997305192", "139.79078800000002"))
print(api.geo_search("Tokyo"))
print(api.lists_list("_SNQ"))
print(api.lists_members("1517792406514839552"))
print(api.lists_memberships("_SNQ"))
print(api.lists_ownerships("_SNQ"))
print(api.lists_show("1517792406514839552"))
print(api.lists_statuses("1517792406514839552"))
print(api.lists_subscribers("1517792406514839552"))
print(api.lists_subscriptions("_SNQ"))
print(api.search_tweets("ツイート"))
print(api.statuses_lookup(["1488101267243429889", "1516619027288043521"]))
print(api.statuses_retweeters_ids("1488101267243429889"))
print(api.statuses_retweets("1488101267243429889"))
print(api.statuses_show("1488101267243429889"))
print(api.statuses_user_timeline("_SNQ"))
print(api.trends_available())
print(api.trends_closest("35.79449997305192", "139.79078800000002"))
print(api.trends_place("1110809"))
print(api.users_lookup(["_SNQ", "Shadow_Ban_Bot"]))
print(api.users_search("_SNQ"))
print(api.user_show("_SNQ"))

# Twitter API v2 OR Twitter API Private
print(api.user_tweets(screen_name="Twitter")) #print(api.user_tweets(user_id="783214"))
print(api.trend())
print(api.searchbox("Text"))
print(api.topic_search("Text"))
print(api.latest_search("Text"))
print(api.image_search("Text"))
print(api.video_search("Text"))
print(api.user_search("Text"))
print(api.screenname_available("Screenname"))
print(api.get_status("1335886771968741377"))
print(api.shadowban_check(screen_name="Twitter")) #print(api.shadowban_check(user_id="783214"))
```

```python
from Twitter_Frontend_API import API

auth = {'auth_token': '----------------------------------------', 'ct0': '--------------------------------'}
auth = API.Login("Twitter", "Password")
print(auth)

api = API(auth)

print(api.generate_ct0())
print(api.generate_authenticity())
print(api.generate_token())
print(api.user_info(screen_name="Twitter")) #print(api.user_info(user_id="783214"))
print(api.user_tweets(screen_name="Twitter")) #print(api.user_tweets(user_id="783214"))
print(api.trend())
print(api.searchbox("Text"))
print(api.topic_search("Text"))
print(api.latest_search("Text"))
print(api.image_search("Text"))
print(api.video_search("Text"))
print(api.user_search("Text"))
print(api.screenname_available("Screenname"))
print(api.get_status("1335886771968741377"))
print(api.update_status("Text"))
print(api.update_status("Text", conversation_control=2, in_reply_to_status_id="1335886771968741377", card_uri="card://1338528317587124224"))
print(api.destroy_status("1335886771968741377"))
print(api.get_dm())
print(send_dm('Text', screen_name="hogehoge")) #print(api.send_dm('Text', user_id="123456"))
print(delete_dm(conversation_id_1=<int:hogehoge1>, conversation_id_2=<int:hogehoge2>)) #https://twitter.com/messages/<int:hogehoge1>-<int:hogehoge2>
print(api.create_favorite("1335886771968741377"))
print(api.destroy_favorite("1335886771968741377"))
print(api.retweet("1335886771968741377"))
print(api.unretweet("1335886771968741377"))
print(api.create_friendship(screen_name="Twitter")) #print(api.create_friendship(user_id="783214"))
print(api.destroy_friendship(screen_name="Twitter")) #print(api.destroy_friendship(user_id="783214"))
print(api.notifications())
print(api.pin_tweet("1335886771968741377"))
print(api.change_id("Screen_name"))
print(api.topic_follow("847896929698668544"))
print(api.topic_unfollow("847896929698668544"))
print(api.followed_topics("1323603354165993472"))
print(api.not_interested_topics())
print(api.recommendations())
print(api.lists_all("1323603354165993472"))
print(api.create_list("ListName", private="False", description=""))
print(api.destroy_list("1337433856673075206"))
print(api.update_list("1326095394959360001", name="NameList", private="True", description="Text"))
print(api.add_list_member("1326095394959360001", "1323603354165993472"))
print(api.remove_list_member("1326095394959360001", "1323603354165993472"))
print(api.list_members("1326095394959360001"))
print(api.create_card(4, "5", one="Hello", two="World", three="!", four="byPython")
print(api.Twitter_Web_Client("Text", place_id="fc6282dff859b848", authenticity_token=None))
print(api.add_bookmark("1335886771968741377"))
print(api.mute_conversation("1335886771968741377"))
print(api.unmute_conversation("1335886771968741377"))
print(api.verify_password("password"))
print(api.account_data(verify=None, password="password"))
print(api.private("true"))
print(api.gender("male"))
print(api.protect_password_reset("password", protect="true"))
print(api.session_revoke("KRJlliMG5b61wbuY4f70nk6TylRkYPJaMmCLT5eiQe8="))
print(api.sessions_revoke_all())
print(api.allow_media_tagging("all"))
print(api.nsfw("true"))
print(api.geo_enabled("true"))
print(api.geo_delete())
print(api.display_sensitive_media("true"))
print(api.twitter_interests())
print(api.set_explore("true"))
print(api.shadowban_check(screen_name="Twitter")) #print(api.shadowban_check(user_id="783214"))
print(api.change_password("old_password", "new_password"))
```

## Donate

Bitcoin Address
16TCmq3QrAmuJied6KwNGuiqxuGpZDVVMp

## Legal
This is not official on Twitter. Use at your own risk.
