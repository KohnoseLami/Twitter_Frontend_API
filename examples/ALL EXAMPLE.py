from Twitter_Frontend_API import Client

api = Client()

print(api.generate_token())
print(api.user_info(screenname="Twitter")) #print(api.user_info(userid="783214"))
print(api.user_tweets(screenname="Twitter")) #print(api.user_info(userid="783214"))
print(api.trend())
print(api.searchbox("Text"))
print(api.topic_search("Text"))
print(api.latest_search("Text"))
print(api.image_search("Text"))
print(api.video_search("Text"))
print(api.user_search("Text"))
print(api.screenname_available("Screenname"))

input()