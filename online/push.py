

import requests
from datetime import datetime

def push_url_to_server(url):
    # 
    server_endpoint = "http://47.107.69.67:80/image"

    # 
    json_data = {
        "picUrl": url,
        "deviceId": "1005",
        "recordId": "2001",
    }

    try:
        # 
        response = requests.post(server_endpoint, json=json_data)

        # 
        if response.status_code == 200:
            print("success")
        else:
            print(f"unsuccess: {response.status_code}")

    except Exception as e:
        print(f"err: {e}")

# 使用上述代码推送图片URL
picture_url = "your_url"  # 
push_url_to_server(picture_url)
