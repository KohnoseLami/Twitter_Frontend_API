# -*- coding: utf-8 -*-
from Twitter_Frontend_API import Client

#ログイン無しでの情報取得
client = Client()
print(client.generate_ct0())
print(client.generate_authenticity())
print(client.generate_token())
print(client.user_info(screen_name="Twitter")) #print(api.user_info(user_id="783214"))
print(client.user_tweets(screen_name="Twitter")) #print(api.user_tweets(user_id="783214"))
print(client.trend())
print(client.searchbox("Text"))
print(client.topic_search("Text"))
print(client.latest_search("Text"))
print(client.image_search("Text"))
print(client.video_search("Text"))
print(client.user_search("Text"))
print(client.screenname_available("Screenname"))
print(client.get_status("1335886771968741377"))
print(client.shadowban_check(screen_name="Twitter")) #print(api.shadowban_check(user_id="783214"))


from Twitter_Frontend_API import API

#ログインと認証情報の定義
#認証情報は辞書形式での定義
auth = {'auth_token': '----------------------------------------', 'ct0': '--------------------------------'}
auth = API.Login("Twitter", "Password")
print(auth)

#ログインあり
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