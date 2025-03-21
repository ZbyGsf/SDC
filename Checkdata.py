import requests
from json.decoder import JSONDecodeError
import numpy as np
from datetime import datetime
from dateutil import relativedelta
import matplotlib.pyplot as plt
result_index_m_dict={1537280853870166018: 0, 
                     1548511911429140481: 1, 
                     1548511911429140482: 2, 
                     1548926457067106305: 3, 
                     1548926457067106311: 4, 
                     1548926457100660737: 5, 
                     1548926457100660738: 6, 
                     1548926457100660741: 7,
                     1548926457113243650: 8, 
                     1550137558513606660: 9, 
                     1550137558584909842: 10, 
                     1550137558584909843: 11, 
                     1550520622469206021: 12, 
                     1550520622481788934: 13, 
                     1558778639210582017: 14, 
                     1558778639210582022: 15, 
                     1558778639210582024: 16, 
                     1559809506712248321: 17, 
                     1559809506720636936: 18, 
                     1562978855400804353: 19, 
                     1569525123832922113: 20, 
                     1569525123849699331: 21, 
                     1569525123858087941: 22, 
                     1613435212482994178: 23}
def calculate_index_from_time(start_time_str, target_time_str):
    # 将起始时间和目标时间字符串转换为 datetime 对象
    start_time_obj = datetime.strptime(start_time_str, '%Y%m%d%H')
    target_time_obj = datetime.strptime(target_time_str, '%Y%m%d%H')
    # 使用 relativedelta 计算两个时间之间的差异
    delta = relativedelta.relativedelta(target_time_obj, start_time_obj)
    # 计算总小时差
    total_hours_difference = (delta.years * 12 + delta.months) * 30 * 24 + delta.days * 24 + delta.hours
    return int(total_hours_difference)
def plot_three_color_heatmap(matrix):
    # 处理矩阵
    processed_matrix = np.where(matrix < 1, 0, np.where(matrix > 1, 2, matrix))
    # 获取矩阵中存在的唯一值
    unique_values = np.unique(processed_matrix).astype(int)
    # 生成颜色映射
    colors = ['red', 'green', 'black']
    cmap = plt.cm.colors.ListedColormap([colors[val] for val in unique_values])

    # 设置图形大小
    plt.figure(figsize=(10, 6))
    # 绘制热力图
    ax = plt.gca()
    im = ax.imshow(processed_matrix, cmap=cmap, aspect='auto')
    # 显示颜色条
    cbar = plt.colorbar(im, ticks=unique_values, label='Value')
    # 如果需要，反转y轴方向
    ax.invert_yaxis()    
    # 显示图表
    plt.show()

# 定义 Flask 应用运行的地址
flask_url = 'http://47.107.69.67:8080/get_data'
# 构建查询条件字符串
starttime = '2024011700'
endtime = '2024012500'

condition_string = (
    f"((year='{starttime[:4]}' and month>='{starttime[4:6]}' and day>='{starttime[6:8]}' and hour>='{starttime[8:10]}') or "
    f"(year='{starttime[:4]}' and month>'{starttime[4:6]}') or "
    f"(year>'{starttime[:4]}')) and "
    f"((year='{endtime[:4]}' and month<='{endtime[4:6]}' and day<='{endtime[6:8]}' and hour<='{endtime[8:10]}') or "
    f"(year='{endtime[:4]}' and month<'{endtime[4:6]}') or "
    f"(year<'{endtime[:4]}'))"
)

try:
    # 发送 POST 请求
    response = requests.post(flask_url, json={'condition': condition_string})

    # 检查响应状态码
    response.raise_for_status()

    # 尝试解析 JSON
    result = response.json()
    
    draw_matrix = np.zeros((24,calculate_index_from_time(starttime, endtime)+1))
    if 'result' in result:
        print(len(result['result']))
        for row in result['result']:
            result_time = row[2] + row[3] + row[4] + row[5]
            result_index_n = calculate_index_from_time(starttime, result_time)
            result_index_m = result_index_m_dict.get(int(row[1]))
            draw_matrix[result_index_m,result_index_n] += 1
    else:
        print('Error:', result)

except JSONDecodeError:
    print('Error: Unable to decode JSON from the response content.')

except requests.exceptions.RequestException as e:
    print(f'Request error: {e}')

plot_three_color_heatmap(draw_matrix)