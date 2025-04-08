
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# 


@app.route('/get_data', methods=['POST'])
def get_data():
    data = request.get_json()

    # 
    condition = data.get('condition')
    connection = sqlite3.connect('your_database.db')
    cursor = connection.cursor()
    # 
    cursor.execute(f"SELECT * FROM object_result WHERE {condition}")
    rows = cursor.fetchall()

    # 
    return jsonify({'result': rows})


