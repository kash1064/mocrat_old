import requests

from mocrat_config.environ_config import env
from mocrat_config.post_texts import *

base_url = env("BASE_URL")

# TODO : post_texts
# error_notifier(sys.exc_info()[0], e.args)
def error_notifier(error_obj, e):
    mocrat_notice_webhook_url = env("MOCRAT_NOTICE_WEBHOOK")

    discord_post_url = env("DISCORD_POST_API")
    discord_payload = {
        "text": error_notice + str(error_obj) + "\n" + str(e),
        "discord_webhook_url": mocrat_notice_webhook_url
    }
    requests.post(base_url + discord_post_url, json=discord_payload, headers = {"Authorization": "JWT " + env('ADMIN_TOKEN')})

if __name__ == "__main__":
    pass
