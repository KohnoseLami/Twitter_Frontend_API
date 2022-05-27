from main import Client

# res = Client().rate_limit_status()
# res = Client().collections_entries("custom-539487832448843776")
# res = Client().favorites_list("_SNQ")
# res = Client().followers_ids("_SNQ")
# res = Client().followers_list("_SNQ")

res = Client().followers_list("_SNQ")

print(res)