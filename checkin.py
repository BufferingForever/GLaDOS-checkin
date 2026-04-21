import requests
import os

def send_telegram(message):
    token = os.environ.get('TG_TOKEN')
    chat_id = os.environ.get('TG_ID')
    
    if not token or not chat_id:
        print('⚠️ 未配置 Telegram 通知，跳过。')
        return

    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'Markdown'
    }
    try:
        r = requests.post(url, json=data)
        if r.status_code == 200:
            print('✅ Telegram 通知发送成功')
        else:
            print(f'❌ Telegram 发送失败: {r.text}')
    except Exception as e:
        print(f'❌ Telegram 请求异常: {e}')

def checkin():
    cookie = os.environ.get('GLADOS_COOKIE')
    
    if not cookie:
        return "❌ 错误: 未在 Secrets 中配置 GLADOS_COOKIE"

    url = "https://railgun.info/api/user/checkin"
    headers = {
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://railgun.info',
        'referer': 'https://railgun.info/console/checkin'
    }
    payload = {'token': 'railgun.info'} 

    try:
        print("⏳ 开始签到...")
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code != 200:
            return f"❌ 请求失败，状态码: {response.status_code}"

        res_json = response.json()
        code = res_json.get('code')
        msg = res_json.get('message')

        # 状态判定
        if code == 0:
            return f"✅ 签到成功\n信息: {msg}"
        elif code == 1:
            return f"🟡 今天已签到\n信息: {msg}"
        elif code == -2:
            return f"❌ Cookie 已过期\n信息: {msg}"
        else:
            return f"❓ 未知状态 (Code: {code})\n信息: {msg}"

    except Exception as e:
        return f"❌ 脚本执行异常: {e}"

# -------------------------------------------------------------------------------------------
# 主程序入口
# -------------------------------------------------------------------------------------------
if __name__ == '__main__':
    # 1. 执行签到
    result = checkin()
    print(result)
    
    # 2. 发送通知
    title = "🤖 GLaDOS 自动签到报告"
    send_telegram(f"*{title}*\n------------------\n{result}")
