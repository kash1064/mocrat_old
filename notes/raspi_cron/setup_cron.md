# Raspi の cron を設定する

## 設定
```
sudo crontab -u ubuntu -e
sudo service cron restart
```

## トラブルシューティング
- cron ログで、cron の動作確認
```
tail -f /var/log/cron.log
```

- 任意のログで影響確認
