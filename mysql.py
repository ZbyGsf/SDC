import sqlite3
import json
from datetime import datetime
import numpy as np
import os

def create_database(db_filename):
    connection = sqlite3.connect(db_filename)
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS processed_images (image_name TEXT PRIMARY KEY);')
    connection.commit()
    connection.close()

def save_dicts_to_db(dicts, db_filename='/home/admin/marine_rubbish_online/DB/object_result.db'):
# def save_dicts_to_db(dicts, db_filename='DB/object_result.db'):
    # 获取当前时间，并将其格式化为字符串，只保留小时部分
    current_time = datetime.now().strftime('%Y-%m-%d %H:00:00')

    # 连接到数据库（如果不存在，将会创建一个新的数据库文件）
    connection = sqlite3.connect(db_filename)
    
    # 创建游标对象，用于执行 SQL 语句
    cursor = connection.cursor()
    
    # 创建数据库表（如果不存在）
    cursor.execute('''CREATE TABLE IF NOT EXISTS object_result
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       deviceId TEXT,
                       year TEXT, 
                       month TEXT, 
                       day TEXT, 
                       hour TEXT, 
                       respic_url TEXT,
                       foam TEXT, 
                       bag TEXT, 
                       branch TEXT, 
                       bottle TEXT,
                       result TEXT,
                       recordId TEXT,
                       timestamp TEXT)''')
    
    # 插入数据到数据库表中
    for my_dict in dicts:
        # 使用参数化查询，避免 SQL 注入攻击
        result_str = json.dumps(my_dict['result'].tolist()) if 'result' in my_dict else None
        cursor.execute("INSERT INTO object_result (deviceId, year, month, day, hour, respic_url, foam, bag, branch, bottle, result, recordId, timestamp) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       ( my_dict['deviceId'], 
                        my_dict['year'],my_dict['month'], my_dict['day'], 
                        my_dict['hour'], my_dict['respic_url'], 
                        my_dict['foam'], my_dict['bag'], my_dict['branch'], my_dict['bottle'], result_str, 
                        my_dict['recordId'],current_time))   
    # 提交事务
    connection.commit()
    # 关闭数据库连接
    connection.close()
    
def get_processed_images_from_db(db_filename='DB/processed_images.db'):
    # if not os.path.exists(db_filename):
    #     # 如果数据库文件不存在，创建一个新的数据库文件
    #     create_database(db_filename)
    connection = sqlite3.connect(db_filename)
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS processed_images (image_name TEXT PRIMARY KEY);')
    cursor.execute('SELECT image_name FROM processed_images;')
    processed_images = set(row[0] for row in cursor.fetchall())
    connection.close()
    return processed_images

def update_processed_images_to_db(new_images, db_filename='DB/processed_images.db'):
    connection = sqlite3.connect(db_filename)
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS processed_images (image_name TEXT PRIMARY KEY);')
    for image in new_images:
        cursor.execute('INSERT INTO processed_images (image_name) VALUES (?);', (image,))
    connection.commit()
    connection.close()

if __name__ == '__main__':
    print("please try !")
