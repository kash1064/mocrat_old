import requests

from config.common_logger import *
from config.environ_config import env

# TODO: ログを追加する
def call_talk_api(query):
    app_logger.info("Call call_talk_api")

    talk_api_url = env("TALK_API_URL")
    payload = {
        "apikey": env("TALK_API_KEY"),
        "query": query,
    }
    response = requests.post(talk_api_url, data=payload)
    app_logger.info("Talk API response is {}".format(str(response.json())))
    return response.json()["results"][0]["reply"]

if __name__ == "__main__":
    pass