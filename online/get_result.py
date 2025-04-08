import requests
from json.decoder import JSONDecodeError

# 
flask_url = 'your_flask_url/get_data'

# 
condition_string = f"year='2024' AND month='03' AND day='18'"

try:
    # 
    response = requests.post(flask_url, json={'condition': condition_string})

    # 
    response.raise_for_status()

    # 
    result = response.json()

    # 
    if 'result' in result:
        for row in result['result']:
            print(row)
    else:
        print('Error:', result)

except JSONDecodeError:
    print('Error: Unable to decode JSON from the response content.')

except requests.exceptions.RequestException as e:
    print(f'Request error: {e}')