import requests

from mocrat_config.environ_config import env
from mocrat_config.post_texts import *

base_url = env("BASE_URL")

# TODO : post_texts
def error_notifier(e):
    mocrat_notice_webhook_url = env("MOCRAT_NOTICE_WEBHOOK")

    discord_post_url = env("DISCORD_POST_API")
    discord_payload = {
        "discord_webhook_url": mocrat_notice_webhook_url,
        "text": error_notice + str(e)
    }
    requests.post(base_url + discord_post_url, json=discord_payload)

if __name__ == "__main__":
    pass
