# YayBot

### YayBot とは？

SNS「Yay!」の非公式ライブラリです。🚀  
使用言語は Python です。

🔗: https://yay.space/

### 重要

まだ開発途中であり、今後も機能の追加を予定中です。  
機能の修正や追加要望等あれば、以下から連絡してください。

---

### [Yay!アカウント](https://yay.space/user/3851771) | [メールアドレス](mailto:nikola.desuga@gmail.com?subject=[GitHub]%20Source%20Han%20Sans)

---

![yay.space](https://yay.space/images/home-group-categories-background-3.jpg)

![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)

## インストール

Requests, BeautifulSoup, tqdm, python-dotenv, huepy をインストールした上で、以下のコマンドをターミナル上で実行してください。

```bash
pip install git+https://github.com/qualia-5w4/Yay-Bot
```

## 使い方

```python
from yaybot import Yay


yay = Yay()

yay.login(email='メールアドレス', password='パスワード') # ログイン


user = yay.get_user('123')  # IDが'123'のユーザーのプロフィールを取得
print(user.screen_name)  # 取得したユーザーの名前を表示
print(user.bio)  # 取得したユーザーの自己紹介を表示


post = yay.get_post('456')  # IDが'456'の投稿を取得
print(post.author_screen_name)  # 投稿者の名前を表示
print(post.text)  # 投稿本文を表示
yay.like_post(post.id)  # 投稿をいいねする


followers = yay.get_user_followers('123')  # IDが'123'のユーザーのフォロワーを取得する
for follower in followers:
    yay.follow_user(follower.id)  # 取得したユーザーをフォローする

```

## 使用条件

- この API をマーケティング目的（スパム、ボット、嫌がらせ、大量の一斉送信など）に使用しないこと。

## 注意

このコードは、「Yay!」、株式会社ナナメウエ、またはその関連会社といかなる関係も持っていません。これは独立した非公式 API です。自己責任で使用してください。

This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by Yay!, Nanameue inc. or any of its affiliates or subsidiaries. This is an independent and unofficial API. Use it at your own risk.
