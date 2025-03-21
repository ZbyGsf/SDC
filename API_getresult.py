
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# 连接到数据库


@app.route('/get_data', methods=['POST'])
def get_data():
    data = request.get_json()

    # 从 JSON 数据中提取查询条件
    condition = data.get('condition')
    connection = sqlite3.connect('/home/admin/marine_rubbish_online/DB/object_result.db')
    cursor = connection.cursor()
    # 执行查询操作
    cursor.execute(f"SELECT * FROM object_result WHERE {condition}")
    rows = cursor.fetchall()

    # 返回结果
    return jsonify({'result': rows})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # app.run(port=5000, debug=True)
