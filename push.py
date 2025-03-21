

import requests
from datetime import datetime

def push_url_to_server(url):
    # 构建请求参数，这里假设您的服务器端点是 "/push_url"
    server_endpoint = "http://47.107.69.67:80/image"

    # 构建请求体
    json_data = {
        "picUrl": url,
        "deviceId": "1005",
        "recordId": "2001",
    }

    try:
        # 发送 POST 请求
        response = requests.post(server_endpoint, json=json_data)

        # 检查响应状态码
        if response.status_code == 200:
            print("URL推送成功")
        else:
            print(f"URL推送失败，状态码: {response.status_code}")

    except Exception as e:
        print(f"发生异常: {e}")

# 使用上述代码推送图片URL
picture_url = "http://218.85.23.37:20149/maritimechart/upload/20231222/94c81c1a08974fb4116f379416ff6683.jpg"  # 请替换为实际的图片 URL
# picture_url = "https://picsum.photos/300/300"
push_url_to_server(picture_url)
