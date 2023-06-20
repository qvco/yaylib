<p align="center">
  <a href="https://github.com/qvco/yaylib">
    <img src="https://github.com/qvco/yaybot/assets/77382767/ea451824-43c1-478c-b7d0-7d34ef587c2e" alt="Logo">
  </a>
  <p align="center">
    <img src="https://img.shields.io/github/release/qualia-5w4/yaybot">
    <img src="https://img.shields.io/badge/python-3.11-blue.svg">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg">
  </p>

  <h3 align="center">Yay! - 非公式ライブラリ</h3>

  <p align="center">
    汎用的な機能を備えた、SNS「Yay!」の非公式APIです。<br />
    とてもシンプルな記述で実装できます。<br />
    <br />
    <a href="https://github.com/qvco/yaylib"><strong>※ 改良版のライブラリはこちらから >></strong></a>
    <br />
    <br />
    <a href="#handshake-共同開発について">開発に参加する</a>
    ·
    <a href="https://yay.space/user/3851771">Yay!アカウント</a>
      ·
    <a href="mailto:nikola.desuga@gmail.com">メールアドレス</a>
  </p>
</p>

<details open>
  <summary>- - - 目次 - - -</summary>
  <ol>
    <li>
      <a href="#このライブラリについて">このライブラリについて</a>
      <ul>
        <li><a href="#改良版ライブラリyaylibへ">改良版ライブラリ「yaylib」へ</a></li>
      </ul>
    </li>
    <li>
      <a href="#-使用方法">使用方法</a>
      <ul>
        <li><a href="#-ダウンロード">ダウンロード</a></li>
        <li><a href="#%EF%B8%8F-始め方">始め方</a></li>
      </ul>
    </li>
    <li><a href="#trophy-機能--特徴">機能 & 特徴</a></li>
    <li><a href="#handshake-共同開発について">共同開発について</a></li>
    <li><a href="#scroll-ライセンス--免責事項">ライセンス & 免責事項</a></li>
  </ol>
</details>

## このライブラリについて

このライブラリは現在開発やメンテナンスを行っていません。代わりに、改良版のプロジェクト「**yaylib**」にて開発を進めています。yaylibでは、以下のような改善が行われています。

- 機能の追加・改善
- パフォーマンスの向上
- 複数人での共同開発

### 改良版ライブラリ「yaylib」へ

改良バージョンのライブラリはこちらになります。ぜひご利用ください。

https://github.com/qvco/yaylib

プロジェクトの貢献については<a href="https://github.com/qvco/yaylib/blob/main/CONTRIBUTING.md">こちら</a>をご覧ください。

## ☕ 使用方法

### 💻 ダウンロード

次のコマンドをターミナル上で実行してください:

```bash
git clone https://github.com/qvco/yaybot

cd yaybot

pip install -r requirements.txt

pip install -e .
```

### 🖥️ 始め方

1. `from yaybot import Yay` でインポートします。
2. ログインは任意ですが、一部の機能が制限されます。

```python
from yaybot import Yay

yay = Yay()

yay.login(email='abcd@example.com', password='pw%?123')

print('access_token: ' + yay.access_token)
print('api_key: ' + yay.api_key)
print('logged_in_as: ' + yay.logged_in_as)

>>> 'access_token: 3270a4ad5djf8eb...'
>>> 'api_key: 928164ea82e4ebc...'
>>> 'logged_in_as: 3851771'
```

3. `yay = Yay(access_token='トークン')` でアクセストークンを使用します。

```python
from yaybot import Yay

yay = Yay(access_token='アクセストークン')

post_ids = ['73628', '73646', '73682']

yay.like_posts(post_ids)

>>> '{"result": "success", "liked_ids": [73628, 73646, 73682]}'
```

4. 属性名を指定して目的のデータを取得します。

```python
from yaybot import Yay

yay = Yay()

user = yay.get_user('123')
print('ユーザー名: ' + user.username)
print('自己紹介: ' + user.bio)

>>> 'ユーザー名: たろう'
>>> '自己紹介: 今日も一日ねむい'
```

5. フォロワーを全員フォローする場合の例

```python
from yaybot import Yay

yay = Yay()
yay.login()

followers = yay.get_user_followers('123')

for follower in followers:
    yay.follow_user(follower.id)

>>> '{"result": "success"}, ...'
```

他にもたくさん機能があるので<strong><a href="https://github.com/qualia-5w4/yaybot/tree/master/examples">詳細はこちら</a></strong>を参照してください。

---

## :trophy: 機能 & 特徴

- シンプルな記述で実装可能
- 汎用的な機能
- プロキシをサポート: http/s

---

## :handshake: 共同開発について

こちらのレポジトリは個人で作成したライブラリです。  
改良版のライブラリとして、現在「<strong><a href="https://github.com/qvco/yaylib">yaylib</a></strong>」の共同開発を行っています。  
開発に参加する場合は、https://github.com/qvco/yaylib にプルリクエストを送信するか、nikola.desuga@gmail.com までご連絡ください。
  
いつでも大歓迎です<33

---

## :scroll: ライセンス & 免責事項

このコードは株式会社ナナメウエ、またはその関連会社といかなる関係も持っていません。これは独立した非公式 API です。**自己責任で使用してください。**

This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by Nanameue inc. or any of its affiliates or subsidiaries. This is an independent and unofficial API. **USE IT AT YOUR OWN RISK.**

Licensed under the [MIT License](LICENSE)
