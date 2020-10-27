# Twitter API を利用可能にする

## 設定方法
- データベースのマイグレーション
```
make makemigrations
make migrate
```

- 管理サイトにログイン
- social application でTwitterを作成し、クライアントKeyとシークレットKeyを入力
- 連携したいTwitterアカウントにアクセスした状態で、/auth/twitter/login/ にアクセス