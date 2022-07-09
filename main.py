import os

from cloud_189_checkin import *
from push_message.push_message import *
from glados_checkin.glados import glados

split_str = '&@@&'

if __name__ == '__main__':
    # glados平台cookie
    glados_cookie = os.environ['GLADOS_COOKIE']
    # 天翼云盘cookie
    cloud189_cookie = os.environ['CLOUD189_COOKIE']
    # pushplus平台token
    pushplus_token = os.environ['PUSHPLUS_TOKEN']
    # server酱token
    server_token = os.environ['SERVER_TOKEN']

    account_checkin_message = []
    checkin_message = []

    # gloads 执行签到
    if glados_cookie is not None and len(glados_cookie) > 0:
        glados_cookies = glados_cookie.split(split_str)
        # 遍历cookie执行签到，并返回签到状态码和签到信息
        for idx, cookie in enumerate(glados_cookies):
            print(f"【Gloads_Account_{idx + 1}】:")
            account_checkin_message = glados(cookie)

            # 存在账户签到信息，说明成功执行了签到
            if account_checkin_message is not None and len(account_checkin_message) > 0:
                checkin_message.append(f"【Gloads_Account_{idx + 1}】 checkin message:" + account_checkin_message + "\n")

    # 天翼云盘执行签到
    if cloud189_cookie is not None and len(cloud189_cookie) > 0:
        cloud189_cookies = cloud189_cookie.split(split_str)
        # 遍历cookie执行签到，并返回签到状态码和签到信息
        for idx, cookie in enumerate(cloud189_cookies):
            print(f"【Cloud189_Account_{idx + 1}】:")
            account_checkin_message = cloud189_checkIn(cookie)

            # 存在账户签到信息，说明成功执行了签到
            if account_checkin_message is not None and len(account_checkin_message) > 0:
                checkin_message.append(f"【Cloud189_Account_{idx + 1}】 checkin message:" + str(account_checkin_message[:]) + "\n")

    # 所有账号签到完毕，判断是否有签到信息，如果有签到信息说明账号执行了签到
    if checkin_message is not None and len(checkin_message) > 0:
        try:
            # 推送签到消息至pushplus平台
            if pushplus_token is not None and len(pushplus_token) > 0:
                pushplus_message(pushplus_token, ''.join(checkin_message))
            else:
                print('The pushplus_token is none')
            #     推送至server酱
            if server_token is not None and len(server_token) > 0:
                server_messgae(token=server_token, title='checkIn status', message=''.join(checkin_message))
            else:
                print('The server_token is none')
        except Exception:
            print('push message error')
