import yaylib

api = yaylib.Client()

api.login(email="", password="")

api.create_post(
    # IDが 123 のユーザーをメンションする場合
    text=f"{api.mention(123)}さん、お元気ですか？"
)
