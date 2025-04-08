# 读指定地址的.db 文件
import sqlite3
import json
from datetime import datetime
import os

# def get_processed_images_from_db(db_filename='DB/processed_images.db'):

import sqlite3
import numpy as np

db_filename = 'DB/object_result.db'
connection = sqlite3.connect(db_filename)
cursor = connection.cursor()

# 
cursor.execute('SELECT * FROM object_result;')

# 
all_rows = cursor.fetchall()

# 
for row in all_rows:
    result_str = row[11]  # 
    result_array = np.array(json.loads(result_str)) if result_str else None
    print("Original Result Array:", result_array)

# 
connection.close()

