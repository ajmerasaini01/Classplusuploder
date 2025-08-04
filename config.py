import os

api_id = int(os.environ.get("api_id"))
api_hash = os.environ.get("api_hash")
bot_token = os.environ.get("bot_token")
auth_users = set(map(int, os.environ.get("auth_users", "").split()))
sudo_users = set(map(int, os.environ.get("sudo_users", "").split()))
