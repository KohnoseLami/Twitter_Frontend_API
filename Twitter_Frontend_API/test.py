from main import Client

res = Client().rate_limit_status()

print(res)