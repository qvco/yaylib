<div><a id="readme-top"></a></div>
<p align="center">
    <img src=https://img.shields.io/github/stars/qvco/yaylib?style=for-the-badge&logo=appveyor&color=blue />
    <img src=https://img.shields.io/github/forks/qvco/yaylib?style=for-the-badge&logo=appveyor&color=blue />
    <img src=https://img.shields.io/github/issues/qvco/yaylib?style=for-the-badge&logo=appveyor&color=informational />
    <img src=https://img.shields.io/github/issues-pr/qvco/yaylib?style=for-the-badge&logo=appveyor&color=informational />
</p>
<br />
<p align="center">
    <a href="https://github.com/othneildrew/Best-README-Template">
        <img src="https://github.com/qvco/yaylib/assets/77382767/6e72ec90-b8e9-40bf-a7ad-34fb2ccea0f9" alt="Logo" height="300px">
    </a>
    <!-- <a href="https://github.com/othneildrew/Best-README-Template">
        <img src="https://github.com/qvco/yaylib/assets/77382767/2cdc26e5-7195-4df3-94c5-db840bdd57ff" alt="Logo" height="300">
    </a> -->
    <!-- <a href="https://github.com/othneildrew/Best-README-Template">
        <img src="https://github.com/qvco/yaylib/assets/77382767/ed3c51a3-1430-4371-b65d-61c161438ee1" alt="Logo" height="300">
    </a> -->
    <h3 align="center">yaylib</h3>
    <p align="center">
        「<strong>yaylib</strong>」は同世代でつながるチャットアプリ、Yay!（イェイ）の API クライアントです。<br />
        このライブラリを使用することで、あらゆる操作の自動化や、ボットの開発が可能です。
        <br />
        <br />
        <a href="https://github.com/qvco/yaylib">
            <strong>詳しい機能の詳細や使い方はこちらから »</strong>
        </a>
        <br />
        <br />
        <a href="https://github.com/qvco/yaylib/issues">Report Bug</a>
        ·
        <a href="https://github.com/qvco/yaylib/issues">Request Feature</a>
        ·
        <a href="https://discord.gg/MEuBfNtqRN">Join the discord</a>
    </p>
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <!-- <li><a href="#機能--特徴">機能 & 特徴</a></li> -->
    <li><a href="#buy-me-a-coffee">Buy me a coffee</a></li>
    <li><a href="#インストール">インストール</a></li>
    <li><a href="#使用例">使用例</a></li>
    <li><a href="#yaylib-で誕生したロボットたち">yaylib で誕生したロボットたち</a></li>
    <li><a href="#共同開発について">共同開発について</a></li>
    <li><a href="#免責事項">免責事項</a></li>
    <li><a href="#利用許諾">利用許諾</a></li>
  </ol>
</details>

<!-- 機能 & 特徴 -->

<!-- ## 機能 & 特徴

そこは将来何しろこんな参考者というのの時よりしでた。何だか結果に堕落児はよくそのらくたですまでで知っばいるにも影響突き抜けますですば、いっそにもしたましだっます。支を至るたものはなお生涯にちょうどありでする。

Here's why:

- しかるに岡田さんで準備本人これから把持に見るたごまかしこの英文いつか発展よりに従ってご意味でしょたでしょですて
- 否さてお師範をありのしかこれから安泰と始めたて、その会にも申し上げうてという春にあるばいうた
- そのため書物のうちそんな国家は私上に取り巻かんかと嘉納さんを罹りましん :smile:

TODO:

- 非同期処理に対応

Use the `BLANK_README.md` to get started. -->

<p align="right">(<a href="#readme-top">トップに戻る</a>)</p>

<!-- Buy me a coffee -->

## Buy me a coffee

もしこのライブラリが気に入っていただけたら  
私たちに ↓ コーヒー ↓ をお恵みくださいませ！！❤

<a href="https://www.buymeacoffee.com/qvco" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

<!-- インストール -->

## インストール

**※ Python 3.11 かそれ以上のバージョンが必要です。**

ライブラリをインストールするには、以下のコマンドを実行します:

```bash
pip install yaylib
```

開発バージョンをインストールするには、以下の手順を実行します:

```bash
git clone https://github.com/qvco/yaylib

cd yaylib

pip install -r requirements.txt

pip install -e .
```

<!-- 使用例 -->

## 使用例

メールアドレスとパスワードを用いてログイン後、新しく投稿を作成するコードです。

```python
import yaylib

api = yaylib.Client()

api.login_with_email(email="hello@example.com", password="abc123")

api.create_post(text="Hi there.", color=2)
```

より詳細な使用例については、[こちら](https://github.com/qvco/yaylib/blob/master/examples) を参照してください。

<p align="right">(<a href="#readme-top">トップに戻る</a>)</p>

<!-- yaylib で誕生したボットの一覧 -->

## yaylib で誕生したロボットたち

yaylib を用いて開発したロボットがある場合は、ぜひ教えてください！

<table align="center">
    <thead>
        <tr>
            <th>MindReader AI</th>
            <th>Funktion (架空)</th>
            <th>香ばしいボット (架空)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">
                <a href="https://yay.space/user/5855987"><img src="/assets/bot-icons/MindReaderAI.jpg" width="200px"></a>
                <br />
                <p>開発者: <a href="https://yay.space/user/35152">毛の可能性</a></p>
            </td>
            <td align="center">
                <a href="https://yay.space/user/0"><img src="/assets/bot-icons/Funktion.jpg" width="200px"></a>
                <br />
                <p>開発者: <a href="https://yay.space/user/0">ぺゅー</a></p>
            </td>
            <td align="center">
                <a href="https://yay.space/user/0"><img src="/assets/bot-icons/香ばしいボット.jpg" width="200px"></a>
                <br />
                <p>開発者: <a href="https://yay.space/user/0">めんぶれ天然水。</a></p>
            </td>
        </tr>
    </tbody>
</table>

<!-- 共同開発について -->

## 共同開発について

私たちと一緒に開発することに興味を持っていただけているなら大歓迎です。

- <a href="https://github.com/qvco/yaylib/pulls">プルリクエストを送信する</a>
- nikola.desuga@gmail.com にメールを送信する
- <a href="https://discord.gg/MEuBfNtqRN">Discord サーバーに参加する</a>

のいずれかの方法でコンタクトしてください！

<!-- サポート -->

<!-- ## サポート

Whether you use this project, have learned something from it, or just like it, please consider supporting it by buying me a coffee, so I can dedicate more time on open-source projects like this :)

<a href="https://www.buymeacoffee.com/" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a> -->

<!-- 免責事項 -->

## 免責事項

yaylib は、API の公式なサポートやメンテナンスを提供するものではありません。このクライアントを使用する場合、利用者は**リスクや責任を自己負担**できるものとします。このクライアントによって提供される情報やデータの正確性、信頼性、完全性、適時性について、いかなる保証も行いません。また、このクライアントの使用によって生じた損害や不利益について、一切の責任を負いかねます。利用者は自己の責任において、このクライアントを使用し、API にアクセスするものとします。なお、この免責事項は予告なく変更される場合があります。

<!-- 利用許諾 -->

## 利用許諾

フルライセンスは [こちら](https://github.com/qvco/yaylib/blob/master/LICENSE) からご確認いただけます。  
このプロジェクトは、 **【MIT ライセンス】** の条件の下でライセンスされています。

<p align="right">(<a href="#readme-top">トップに戻る</a>)</p>
