




## setup
### .envファイル
- mocrat_config 配下に .env ファイルを作成

```
ADMIN_TOKEN=
AUTH_USER_MODEL=mocrat_user.User
BASE_URL=https://chiba-moku2.herokuapp.com/
SECRET_KEY=testhelloworld

DATABASE_URL=
DEBUG=False
DISABLE_COLLECTSTATIC=1

DISCORD_POST_API=mocrat_discord/api/v1/post_text/
DISCORD_TOKEN=
DJANGO_STATIC_HOST=https://chiba-moku2.herokuapp.com
MOCRAT_ASAKATSU_WEBHOOK=
MOCRAT_NOTICE_WEBHOOK=
MOCRAT_INFO_WEBHOOK=
MOCRAT_USER_URL=mocrat_user/api/v1/user/

POSTGRES_HOST=
POSTGRES_NAME=
POSTGRES_PASSWORD=
POSTGRES_PORT=5432
POSTGRES_USER=

TWITTER_API_KEY=
TWITTER_API_SECRET=
TWITTER_CREATE_FAV_API=mocrat_twitter/api/v1/twitter_create_fav_url/
TWITTER_POST_API=mocrat_twitter/api/v1/post_text/
TWITTER_SERCH_QUERY_API=mocrat_twitter/api/v1/search_query_tweets/

HATEBU_IT_TOP_XML_RSS=https://b.hatena.ne.jp/hotentry/it.rss
```