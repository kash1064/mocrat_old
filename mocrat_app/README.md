## mocrat_app
### mocrat_config
> Django の設定ファイルと、管理スクリプト

- Djangoの設定ファイル

- admin_utils
  - error_notify.py

- 環境変数の設定
    - .env
    - environ_config.py
  
- Celeryの設定
  - celery.py

- テキストデータ
  - post_texts.py

### mocrat_user
#### モデル
- カスタムユーザモデル

#### ビュー

### mocrat_discord(/mocrat_discord/api/v1/)
> Discord Webhook を利用するAPI
> Discord bot は discord_app を参照

#### モデル

#### ビュー
- Discord WebhookのAPI呼び出し
  - PostText(post_text/)
    - requires(POST data)
      - discord_webhook_url
      - text

### mocrat_twitter
> Twitter APIを利用するAPI

#### モデル

#### ビュー

### utils
> mocrat の各機能を利用するツール群
> API経由での呼び出し不可

## setup
### .envファイル
- mocrat_config 配下に .env ファイルを作成

```
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