from main import Client

# res = Client().rate_limit_status()
# res = Client().collections_entries("custom-539487832448843776")
# res = Client().favorites_list("_SNQ")
# res = Client().followers_ids("_SNQ")
# res = Client().followers_list("_SNQ")
# res = Client().friends_ids("_SNQ")
# res = Client().friends_list("_SNQ")
# res = Client().friendships_show("_SNQ", "Shadow_Ban_Bot")
# res = Client().geo_id("06ef846bfc783874")
# res = Client().geo_reverse_geocode("35.79449997305192", "139.79078800000002")

res = Client().geo_reverse_geocode("35.79449997305192", "139.79078800000002")

print(res)