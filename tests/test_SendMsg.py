from src.WeChatEnterprise.API.SendMsg import WeChatEnterprise


class TestClass:
    CORP_ID = "ww543db93a8c684d34"
    CORP_SECRET = "-H2Ldym0WdsMXoHVlbeb6EN_T8xdFA4SlZpnGZ30T3k"
    AGENT_ID = "1000003"
    WECHAT_USER = "Alderson"
    REDIS_HOST = "192.168.1.3"
    wechat = WeChatEnterprise(CORP_ID, CORP_SECRET, AGENT_ID, REDIS_HOST)

    def test_upload_media(self):
        response = self.wechat.upload_media("1.txt")
        print(response)
        assert response is not None

    def test_send_text_message(self):
        response = self.wechat.send_text_message("123456")
        print(response.json())
        assert response.json().get('errcode') == 0

    def test_send_file_message(self):
        media_id = self.wechat.upload_media("1.txt")
        response = self.wechat.send_file_message(media_id)
        print(response.json())
        assert response.json().get('errcode') == 0
