import requests
import json
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent()

###例外クラス###
class TwitterError(Exception):
    pass


###ログイン無し情報取得###

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

    def user_info(self, screen_name=None, user_id=None):
        if screen_name == None:
            if user_id == None:
                raise TwitterError("Neither 'screen_name' nor 'user_id' was entered.")
            else:
                response = requests.get('https://api.twitter.com/1.1/users/show.json?user_id=' + user_id, headers=self.headers).json()
        else:
            response = requests.get('https://api.twitter.com/1.1/users/show.json?screen_name=' + screen_name, headers=self.headers).json()

        return response

    def user_tweets(self, screen_name=None, user_id=None):
        params = (
            ('userId', user_id),
        )
        if screen_name == None:
            if user_id == None:
                raise TwitterError("Neither 'screen_name' nor 'user_id' was entered.")
            else:
                response = requests.get('https://api.twitter.com/2/timeline/profile/' + user_id + '.json', headers=self.headers, params=params).json()
        else:
            user_id = requests.get('https://api.twitter.com/1.1/users/show.json?screen_name=' + screen_name, headers=self.headers).json()["id_str"]
            response = requests.get('https://api.twitter.com/2/timeline/profile/' + user_id + '.json', headers=self.headers, params=params).json()

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

    def tweet_info(self, tweetid):
        response = requests.get('https://api.twitter.com/2/timeline/conversation/' + tweetid + '.json', headers=self.headers).json()

        return response

###ログインありアカウント操作###

class API(object):
    def __init__(self, auth):
        self.headersss = {
            'origin': 'https://twitter.com',
            'cookie': 'auth_token=' + auth["auth_token"] + '; ct0=' + auth["ct0"],
            'User-Agent': ua.ie
        }

        self.headers = {
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'x-csrf-token': auth["ct0"],
            'cookie': 'auth_token=' + auth["auth_token"] + '; ct0=' + auth["ct0"],
            'User-Agent': ua.ie
        }

        self.headerss = {
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'x-csrf-token': auth["ct0"],
            'content-type': 'application/json',
            'cookie': 'auth_token=' + auth["auth_token"] + '; ct0=' + auth["ct0"],
            'User-Agent': ua.ie
        }

    def Login(session_u, session_p):
        response = requests.get('https://twitter.com/account/begin_password_reset')
        soup = BeautifulSoup(response.text, "lxml")
        authenticity = soup.find(attrs={'name':'authenticity_token'}).get('value')
    
        headers = {
            'cookie': '_mb_tk=' + authenticity,
            'User-Agent': ua.ie
        }
        
        data = {
          'redirect_after_login': '/',
          'remember_me': '1',
          'authenticity_token': authenticity,
          'session[username_or_email]': session_u,
          'session[password]': session_p
        }
        
        response = requests.post('https://twitter.com/sessions', headers=headers, data=data, allow_redirects=False)
        print(BeautifulSoup(response.text, "html.parser"))
        auth_token = response.cookies.get_dict()["auth_token"]
    
        response = requests.get('https://twitter.com/i/release_notes')
        ct0 = response.cookies.get_dict()["ct0"]
    
        return {'auth_token':auth_token, 'ct0':ct0}

    def update_status(self, text, conversation_control=None, in_reply_to_status_id=None, card_uri=None):
         if in_reply_to_status_id == None:
             if conversation_control == None:
                 if card_uri == None:
                     data = {
                       'status': text
                     }
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()
                 elif not card_uri == None:
                     data = {
                       'card_uri': card_uri,
                       'status': text
                     }
                     
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()

             elif conversation_control == 1:
                 if card_uri == None:
                     data = {
                       'conversation_control': 'community',
                       'status': text
                     }
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()
                 elif not card_uri == None:
                     data = {
                       'card_uri': card_uri,
                         'conversation_control': 'community',
                       'status': text
                     }
                     
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()

             elif conversation_control == 2:
                 if card_uri == None:
                     data = {
                       'conversation_control': 'by_invitation',
                       'status': text
                     }
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()
                 elif not card_uri == None:
                     data = {
                       'card_uri': card_uri,
                         'conversation_control': 'by_invitation',
                       'status': text
                     }
                     
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()

         elif not in_reply_to_status_id == None:
             if conversation_control == None:
                 if card_uri == None:
                     data = {
                       'auto_populate_reply_metadata': 'true',
                       'in_reply_to_status_id': in_reply_to_status_id,
                       'status': text
                     }
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()
                 elif not card_uri == None:
                     data = {
                       'auto_populate_reply_metadata': 'true',
                       'in_reply_to_status_id': in_reply_to_status_id,
                       'card_uri': card_uri,
                       'status': text
                     }
                     
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()

             elif conversation_control == 1:
                 if card_uri == None:
                     data = {
                       'auto_populate_reply_metadata': 'true',
                       'in_reply_to_status_id': in_reply_to_status_id,
                       'conversation_control': 'community',
                       'status': text
                     }
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()
                 elif not card_uri == None:
                     data = {
                       'card_uri': card_uri,
                       'auto_populate_reply_metadata': 'true',
                       'in_reply_to_status_id': in_reply_to_status_id,
                       'conversation_control': 'community',
                       'status': text
                     }
                     
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()

             elif conversation_control == 2:
                 if card_uri == None:
                     data = {
                       'auto_populate_reply_metadata': 'true',
                       'in_reply_to_status_id': in_reply_to_status_id,
                       'conversation_control': 'by_invitation',
                       'status': text
                     }
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()
                 elif not card_uri == None:
                     data = {
                       'card_uri': card_uri,
                       'auto_populate_reply_metadata': 'true',
                       'in_reply_to_status_id': in_reply_to_status_id,
                       'conversation_control': 'by_invitation',
                       'status': text
                     }
                     
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()

         return response

    def destroy_status(self, id):
         data = {
           'id': id
         }
         response = requests.post('https://twitter.com/i/api/1.1/statuses/destroy.json', headers=self.headers, data=data).json()

         return response

    def create_favorite(self, id):
        data = {
          'id': id
        }
        response = requests.post('https://twitter.com/i/api/1.1/favorites/create.json', headers=self.headers, data=data).json()

        return response

    def destroy_favorite(self, id):
        data = {
          'id': id
        }
        response = requests.post('https://twitter.com/i/api/1.1/favorites/destroy.json', headers=self.headers, data=data).json()

        return response

    def retweet(self, id):
        data = {
          'id': id
        }
        response = requests.post('https://twitter.com/i/api/1.1/statuses/retweet.json', headers=self.headers, data=data).json()

        return response

    def unretweet(self, id):
        data = {
          'id': id
        }
        response = requests.post('https://twitter.com/i/api/1.1/statuses/unretweet.json', headers=self.headers, data=data).json()

        return response

    def create_friendship(self, screen_name=None, user_id=None):
        if screen_name == None:
            if user_id == None:
                raise TwitterError("Neither 'screen_name' nor 'user_id' was entered.")
            else:
                data = {
                  'id': user_id
                }

                response = requests.post('https://twitter.com/i/api/1.1/friendships/create.json', headers=self.headers, data=data).json()

        else:
            data = {
              'screen_name': screen_name
            }

            response = requests.post('https://twitter.com/i/api/1.1/friendships/create.json', headers=self.headers, data=data).json()

        return response

    def destroy_friendship(self, screen_name=None, user_id=None):
        if screen_name == None:
            if user_id == None:
                raise TwitterError("Neither 'screen_name' nor 'user_id' was entered.")
            else:
                data = {
                  'id': user_id
                }

                response = requests.post('https://twitter.com/i/api/1.1/friendships/destroy.json', headers=self.headers, data=data).json()

        else:
            data = {
              'screen_name': screen_name
            }

            response = requests.post('https://twitter.com/i/api/1.1/friendships/destroy.json', headers=self.headers, data=data).json()

        return response

    def notifications(self):
        response = requests.get('https://twitter.com/i/api/2/notifications/all.json', headers=self.headers).json()

        return response

    def pin_tweet(self, id):
        data = {
          'id': id
        }

        response = requests.post('https://twitter.com/i/api/1.1/account/pin_tweet.json', headers=self.headers, data=data).json()

        return response

    def unpin_tweet(self, id):
        data = {
          'id': id
        }

        response = requests.post('https://twitter.com/i/api/1.1/account/unpin_tweet.json', headers=self.headers, data=data).json()

        return response

    def change_id(self, id):
        data = {
          'screen_name': id
        }
        
        response = requests.post('https://twitter.com/i/api/1.1/account/settings.json', headers=self.headers, data=data).json()

        return response

    def private(self, protected):
        if not protected.lower() in ["true", "false"]:
            raise TwitterError("""Please enter "true" or "false".""")
        elif protected.lower() in ["true", "false"]:
            data = {
              'protected': protected
            }
            
            response = requests.post('https://twitter.com/i/api/1.1/account/settings.json', headers=self.headers, data=data).json()

        return response

    def gender(self, gender):
        if gender.lower() in ["female", "male"]:
            data = '{"preferences":{"gender_preferences":{"use_gender_for_personalization":true,"gender_override":{"type":"' + gender.lower() + '","value":"' + gender.lower() + '"}}}}'

            response = requests.post('https://twitter.com/i/api/1.1/account/settings.json', headers=self.headers, data=data).json()
        else:
            data = '{"preferences":{"gender_preferences":{"use_gender_for_personalization":true,"gender_override":{"type":"custom","value":"' + gender.lower() + '"}}}}'

        return response

    def protect_password_reset(self, password, protect=None):
        if protect.lower() in ["true", "false"]:
            data = {
              'protect_password_reset': protect,
              'current_password': password
            }
            
            response = requests.post('https://twitter.com/i/api/1.1/account/settings.json', headers=self.headers, data=data).json()

        else:
            raise TwitterError("""Please enter "true" or "false".""")

        return response

    def session_revoke(self, hashed_token):
        data = {
          'hashed_token': hashed_token
        }
        
        response = requests.post('https://twitter.com/i/api/account/sessions/revoke', headers=self.headers, data=data).json()

        return response

    def sessions_revoke_all(self):

        response = requests.post('https://twitter.com/i/api/account/sessions/revoke_all', headers=self.headers).json()

        return response

    def allow_media_tagging(self, allow_level):
        if allow_level.lower() in ["all", "following", "none"]:
            data = {
              'allow_media_tagging': allow_level.lower()
            }

            response = requests.post('https://twitter.com/i/api/1.1/account/settings.json', headers=self.headers, data=data).json()

        else:
            raise TwitterError("""Please enter "all" or "following" or "none".""")

        return response

    def nsfw(self, nsfw):
        if nsfw.lower() in ["true", "false"]:
            data = {
              'nsfw_user': nsfw.lower()
            }

            response = requests.post('https://twitter.com/i/api/1.1/account/settings.json', headers=self.headers, data=data).json()

        else:
            raise TwitterError("""Please enter "true" or "false".""")

        return response

    def geo_enabled(self, geo):
        if geo.lower() in ["true", "false"]:
            data = {
              'geo_enabled': geo.lower()
            }

            response = requests.post('https://twitter.com/i/api/1.1/account/settings.json', headers=self.headers, data=data).json()

        else:
            raise TwitterError("""Please enter "true" or "false".""")

        return response

    def geo_delete(self):
        response = requests.post('https://twitter.com/i/api/1.1/geo/delete_location_data.json', headers=self.headers).json()

        return response

    def display_sensitive_media(self, display):
        if display.lower() in ["true", "false"]:
            data = {
              'display_sensitive_media': display.lower()
            }

            response = requests.post('https://twitter.com/i/api/1.1/account/settings.json', headers=self.headers, data=data).json()

        else:
            raise TwitterError("""Please enter "true" or "false".""")

        return response

    def twitter_interests(self):
        response = requests.get('https://twitter.com/i/api/1.1/account/personalization/twitter_interests.json', headers=self.headers).json()

        return response

    def set_explore(self, places):
        if places.lower() in ["true", "false"]:
            data = {
              'use_current_location': places.lower()
            }

            response = requests.post('https://twitter.com/i/api/2/guide/set_explore_settings.json', headers=self.headers, data=data).json()

        else:
            data = {
              'places': places
            }

            response = requests.post('https://twitter.com/i/api/2/guide/set_explore_settings.json', headers=self.headers, data=data).json()

        return response

    def topic_follow(self, id):
        data = '{"variables":"{\\"topicId\\":\\"' + id + '\\"}"}'

        response = requests.post('https://twitter.com/i/api/graphql/4cBaE5ehyzJ1xr5-AoT5cw/TopicFollow', headers=self.headerss, data=data).json()

        return response

    def topic_unfollow(self, id):
        data = '{"variables":"{\\"topicId\\":\\"' + id + '\\"}"}'

        response = requests.post('https://twitter.com/i/api/graphql/v4k95ijrXpxhwGdTWWNc9g/TopicUnfollow', headers=self.headerss, data=data).json()

        return response

    def followed_topics(self, id):
        params = (
            ('variables', '{"userId":"' + id + '"}'),
        )

        response = requests.get('https://twitter.com/i/api/graphql/sXXi7qCBNBIXxhMLXpMFgQ/FollowedTopics', headers=self.headerss, params=params).json()

        return response

    def not_interested_topics(self):
        response = requests.get('https://twitter.com/i/api/graphql/IynHqLeaa4Xm0TT7JuIZZg/NotInterestedTopics', headers=self.headerss).json()

        return response

    def recommendations(self):
        response = requests.get('https://twitter.com/i/api/1.1/users/recommendations.json', headers=self.headers).json()

        return response

    def lists_all(self, id):
        params = (
            ('variables', '{"userId":"' + id + '","withTweetResult":false,"withUserResult":false}'),
        )
        
        response = requests.get('https://twitter.com/i/api/graphql/zpuJN3UciLfyrdIK-6zuHA/CombinedLists', headers=self.headerss, params=params).json()

        return response

    def create_list(self, name, private="False", description=""):
        data = '{"variables":"{\\"isPrivate\\":' + private.lower() + ',\\"name\\":\\"' + name + '\\",\\"description\\":\\"' + description + '\\",\\"withUserResult\\":false}"}'
        
        response = requests.post('https://twitter.com/i/api/graphql/uUTfBUYah4ct184vDaV2KA/CreateList', headers=self.headerss, data=data).json()

        return response

    def destroy_list(self, id):
        data = '{"variables":"{\\"listId\\":\\"' + id + '\\"}"}'
        
        response = requests.post('https://twitter.com/i/api/graphql/UnN9Th1BDbeLjpgjGSpL3Q/DeleteList', headers=self.headerss, data=data).json()

        return response

    def update_list(self, id, name="", private="False", description=""):
        data = '{"variables":"{\\"listId\\":\\"' + id + '\\",\\"isPrivate\\":' + private.lower() + ',\\"description\\":\\"' + description + '\\",\\"name\\":\\"' + name + '\\",\\"withUserResult\\":false}"}'

        response = requests.post('https://twitter.com/i/api/graphql/9CCuAshk9gX5ceEMhc2H5A/UpdateList', headers=self.headerss, data=data).json()

        return response

    def add_list_member(self, id, user_id):
        data = '{"variables":"{\\"listId\\":\\"' + id + '\\",\\"userId\\":\\"' + user_id + '\\",\\"withUserResult\\":false}"}'
        
        response = requests.post('https://twitter.com/i/api/graphql/1PeyBdMyCv1GtFn10VNL-g/ListAddMember', headers=self.headerss, data=data).json()

        return response

    def remove_list_member(self, id, user_id):
        data = '{"variables":"{\\"listId\\":\\"' + id + '\\",\\"userId\\":\\"' + user_id + '\\",\\"withUserResult\\":false}"}'
        
        response = requests.post('https://twitter.com/i/api/graphql/DsE0uIywHZ52-Itoq2dhSw/ListRemoveMember', headers=self.headerss, data=data).json()

        return response

    def list_members(self, id):
        params = (
            ('variables', '{"listId":"' + id + '","withTweetResult":false,"withUserResult":false}'),
        )
        
        response = requests.get('https://twitter.com/i/api/graphql/l7oY9paKsUYC1IWil9PF_w/ListMembers', headers=self.headerss, params=params).json()

        return response

    def create_card(self, quantity, minutes, one="Hello", two="World", three="!", four="byPython"):
        if quantity == 2:
            data = {
              'card_data': '{"twitter:card":"poll2choice_text_only","twitter:api:api:endpoint":"1","twitter:long:duration_minutes":' + minutes + ',"twitter:string:choice1_label":"' + one + '","twitter:string:choice2_label":"' + two + '"}'
            }

            response = requests.post('https://caps.twitter.com/v2/cards/create.json', headers=self.headers, data=data).json()

        elif quantity == 3:
            data = {
              'card_data': '{"twitter:card":"poll3choice_text_only","twitter:api:api:endpoint":"1","twitter:long:duration_minutes":' + minutes + ',"twitter:string:choice1_label":"' + one + '","twitter:string:choice2_label":"' + two + '","twitter:string:choice3_label":"' + three + '"}'
            }

            response = requests.post('https://caps.twitter.com/v2/cards/create.json', headers=self.headers, data=data).json()

        elif quantity == 4:
            data = {
              'card_data': '{"twitter:card":"poll4choice_text_only","twitter:api:api:endpoint":"1","twitter:long:duration_minutes":' + minutes + ',"twitter:string:choice1_label":"' + one + '","twitter:string:choice2_label":"' + two + '","twitter:string:choice3_label":"' + three + '","twitter:string:choice4_label":"' + four + '"}'
            }

            response = requests.post('https://caps.twitter.com/v2/cards/create.json', headers=self.headers, data=data).json()

        else:
            raise TwitterError("Please specify the number of votes between 2 and 4.")

        return response

    def Twitter_Web_Client(self, text, place_id="", authenticity_token=None):
        if authenticity_token == None:
            response = requests.get('https://twitter.com/account/begin_password_reset')
            soup = BeautifulSoup(response.text, "lxml")
            authenticity_token = soup.find(attrs={'name':'authenticity_token'}).get('value')
            data = {
              'authenticity_token': authenticity_token,
              'batch_mode': 'off',
              'place_id': place_id,
              'status': text,
            }
            
            response = requests.post('https://twitter.com/i/tweet/create', headers=self.headersss, data=data).json()

        elif not authenticity_token == None:
            data = {
              'authenticity_token': authenticity_token,
              'batch_mode': 'off',
              'place_id': place_id,
              'status': text,
            }
            
            response = requests.post('https://twitter.com/i/tweet/create', headers=self.headersss, data=data).json()

        return response

    def add_bookmark(self, id):
        data = {
          'tweet_mode': 'extended',
          'tweet_id': id
        }

        response = requests.post('https://twitter.com/i/api/1.1/bookmark/entries/add.json', headers=self.headers, data=data).json()

        return response

    def mute_conversation(self, id):
        data = {
          'tweet_mode': 'extended',
          'tweet_id': id
        }
        
        response = requests.post('https://twitter.com/i/api/1.1/mutes/conversations/create.json', headers=self.headers, data=data).json()

        return response

    def unmute_conversation(self, id):
        data = {
          'tweet_mode': 'extended',
          'tweet_id': id
        }
        
        response = requests.post('https://twitter.com/i/api/1.1/mutes/conversations/destroy.json', headers=self.headers, data=data).json()

        return response

    def verify_password(self, password):
        data = {
          'password': password
        }
        
        response = requests.post('https://twitter.com/i/api/1.1/account/verify_password.json', headers=self.headers, data=data)

        return response.json() | response.cookies.get_dict()

    def account_data(self, verify=None, password=""):
        if verify == None:
            data = {
              'password': password
            }

            response = requests.post('https://twitter.com/i/api/1.1/account/verify_password.json', headers=self.headers, data=data)
            if "errors" in response.json():
                raise TwitterError(response.json()["errors"][0]["message"])
            elif response.json()["status"] == "ok":
                cookie = self.headers["cookie"] + '; _twitter_sess=' + response.cookies.get_dict()["_twitter_sess"]
                self.headers["cookie"] = cookie

                response = requests.get('https://twitter.com/i/api/1.1/account/personalization/p13n_data.json', headers=self.headers).json()

        elif not verify == None:
            cookie = self.headers["cookie"] + '; _twitter_sess=' + verify
            self.headers["cookie"] = cookie

            response = requests.get('https://twitter.com/i/api/1.1/account/personalization/p13n_data.json', headers=self.headers).json()

        return response
