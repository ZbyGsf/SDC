import requests
from json.decoder import JSONDecodeError

# 定义 Flask 应用运行的地址
flask_url = 'http://47.107.69.67:8080/get_data'

# 构建查询条件字符串
condition_string = f"year='2024' AND month='03' AND day='18'"

try:
    # 发送 POST 请求
    response = requests.post(flask_url, json={'condition': condition_string})

    # 检查响应状态码
    response.raise_for_status()

    # 尝试解析 JSON
    result = response.json()
    # print(result)
    # 处理结果
    if 'result' in result:
        for row in result['result']:
            print(row)
    else:
        print('Error:', result)

except JSONDecodeError:
    print('Error: Unable to decode JSON from the response content.')

except requests.exceptions.RequestException as e:
    print(f'Request error: {e}')