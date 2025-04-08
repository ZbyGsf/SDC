from flask import Flask, request
import os
from datetime import datetime
import requests
import json
from urllib.parse import quote

app = Flask(__name__)

MAX_RETRIES =5
def download_url(url, save_path):

    directory = os.path.dirname(save_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    for attempt in range(MAX_RETRIES):
        headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus 5 Build/MMB29K) tuhuAndroid 5.24.6',
            'content-type': 'application/json'}
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            print(save_path)
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f'Downloaded: {url}')
            return True
        else:
            print(f'Failed to download: {url}, Attempt {attempt + 1}')

    print(f'Maximum retries reached. Failed to download: {url}')
    return False

@app.route("/image", methods=["POST"])

def app_api():
    json_data = request.get_json()

    try:
        picture_url = json_data["picUrl"]
        deviceId = json_data["deviceId"]
        recordId = json_data["recordId"]
        current_time = datetime.now()
        year_month_day = current_time.strftime('%Y%m%d')
        hour = current_time.strftime('%H')

        file_path = os.path.join("/home/admin/down_img", year_month_day, deviceId, f"{hour}_{recordId}.jpg")
        print('1')       
        if os.path.exists(file_path):
            print(f'Skipping already downloaded file: {file_path}')
        else:
            success = download_url(picture_url, file_path)
            print(success)
            attempt_count = 1
            while not success and attempt_count < MAX_RETRIES:
                print(f'Retrying download for {attempt_count} time(s) for: {picture_url}')
                success = download_url(picture_url, file_path)
                attempt_count += 1
            if success:
                with open("url.txt", "a+") as f:
                    f.write(file_path + "\n")
                    f.close()
                    print(f'Updated URL in the text file: {file_path}')

        params = {"code": 0000, "msg": "complete"}
        params = json.dumps(params)
        return params
   
    except:
        params = {"code": 1003, "msg": "picUrl missing or incorrect"}
        params = json.dumps(params)
        return params
