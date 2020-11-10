import requests
import json
from fake_useragent import UserAgent

ua = UserAgent()

class Client:
    headers = {
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'User-Agent': ua.ie
    }
    guest_token = requests.post('https://api.twitter.com/1.1/guest/activate.json', headers=headers).json()["guest_token"]

    headers = {
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'x-guest-token': guest_token,
        'User-Agent': ua.ie
    }

    def generate_token(self):
        headers = {
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'User-Agent': ua.ie
        }
        response = requests.post('https://api.twitter.com/1.1/guest/activate.json', headers=headers).json()

        return response

    def user_info(self, screenname=None, userid=None):
        if screenname == None:
            if userid == None:
                raise Exception("Neither screen name nor user ID was entered.")
            else:
                response = requests.get('https://api.twitter.com/1.1/users/show.json?user_id=' + userid, headers=self.headers).json()
        else:
            response = requests.get('https://api.twitter.com/1.1/users/show.json?screen_name=' + screenname, headers=self.headers).json()

        return response

    def user_tweets(self, screenname=None, userid=None):
        params = (
            ('userId', userid),
        )
        if screenname == None:
            if userid == None:
                raise Exception("Neither screen name nor user ID was entered.")
            else:
                response = requests.get('https://api.twitter.com/2/timeline/profile/' + userid + '.json', headers=self.headers, params=params).json()
        else:
            userid = requests.get('https://api.twitter.com/1.1/users/show.json?screen_name=' + screenname, headers=self.headers).json()["id_str"]
            response = requests.get('https://api.twitter.com/2/timeline/profile/' + userid + '.json', headers=self.headers, params=params).json()

        return response

    def trend(self):
        response = requests.get('https://twitter.com/i/api/2/guide.json', headers=self.headers).json()

        return response

    def searchbox(self, text):
        params = (
            ('q', text),
            ('src', 'search_box'),
        )
        response = requests.get('https://twitter.com/i/api/1.1/search/typeahead.json', headers=self.headers, params=params).json()

        return response

    def topic_search(self, text):
        params = (
            ('q', text),
            ('tweet_search_mode', 'extended'),
        )
        response = requests.get('https://twitter.com/i/api/2/search/adaptive.json', headers=self.headers, params=params).json()

        return response

    def latest_search(self, text):
        params = (
            ('q', text),
            ('tweet_search_mode', 'live'),
        )
        response = requests.get('https://twitter.com/i/api/2/search/adaptive.json', headers=self.headers, params=params).json()

        return response

    def image_search(self, text):
        params = (
            ('q', text),
            ('tweet_mode', 'extended'),
            ('result_filter', 'image'),
        )
        response = requests.get('https://twitter.com/i/api/2/search/adaptive.json', headers=self.headers, params=params).json()

        return response

    def video_search(self, text):
        params = (
            ('q', text),
            ('tweet_mode', 'extended'),
            ('result_filter', 'video'),
        )
        response = requests.get('https://twitter.com/i/api/2/search/adaptive.json', headers=self.headers, params=params).json()

        return response

    def user_search(self, text):
        params = (
            ('q', text),
            ('tweet_mode', 'extended'),
            ('result_filter', 'user'),
        )
        response = requests.get('https://twitter.com/i/api/2/search/adaptive.json', headers=self.headers, params=params).json()

        return response

    def screenname_available(self, id):
        params = (
            ('username', id),
        )
        response = requests.get('https://twitter.com/i/api/i/users/username_available.json', headers=self.headers, params=params).json()

        return response