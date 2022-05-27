from main import Client

# res = Client().rate_limit_status()
# res = Client().collections_entries("custom-539487832448843776")
# res = Client().favorites_list("1218659670")

res = Client().favorites_list("1218659670")

print(res)