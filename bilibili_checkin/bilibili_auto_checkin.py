import requests
import urllib3

bilbi_checkin_url = 'https://api.live.bilibili.com/xlive/web-ucenter/v1/sign/DoSign'


def __get_header(cookie_header):
    header = {
        'Connection': 'Keep-Alive',
        'Accept': '*/*',
        'Accept-Language': 'zh-cn',
        'Cookie': cookie_header,
        'Host': 'api.live.bilibili.com',
        'Content-Type': 'application/json;charset=UTF-8',
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G930K Build/NRD90M; wv)"
                      " AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74"
                      ".0.3729.136 Mobile Safari/537.36 Ecloud/8.6.3 Android/22 clie"
                      "ntId/355325117317828 clientModel/SM-G930K imsi/46007111431782"
                      "4 clientChannelId/qq proVersion/1.0.6",
        "Referer": "https://api.live.bilibili.com/xlive/web-ucenter/v1/sign/DoSign",
        "Accept-Encoding": "gzip, deflate",
    }
    return header


# 解决出现警告 Adding certificate verification is strongly advised.
urllib3.disable_warnings()


def bilibili_checkin(cookie):
    header = __get_header(cookie)
    resp = requests.get(url=bilbi_checkin_url, headers=header, verify=False)
    result = resp.text
    result_json = resp.json()
    resp.close()
    if 'code' in result and 'data' in result and result_json['code'] == 0:
        check_message = '签到成功,获得' + result_json['data']['text']
    elif 'code' in result and result_json['code'] == 1011040:
        check_message = result_json['message']
    else:
        check_message = 'bilibili checkin error'
    print(check_message)
    return check_message
