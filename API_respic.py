from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# 设置图片存储目录
IMAGE_FOLDER = '/home/admin/img'
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

app.logger.setLevel('DEBUG')

@app.route('/images/<path:subpath>/<filename>')
def get_image(subpath,filename):
    full_path = f"{app.config['UPLOAD_FOLDER']}/{subpath}"
    app.logger.info(f"Attempting to access: {full_path}")
    # 检查文件是否存在
    if os.path.exists(full_path):
        return send_from_directory(app.config['UPLOAD_FOLDER'],  f"{subpath}/{filename}")
    else:
        return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

# http://192.168.1.100:5001/images/subpath/subpath/1001.jpg
# http://47.107.69.67:8081/images/20231221/1003/19_https%3A%2F%2Fpicsum.photos%2F200%2F300_1001.jpg

# http://47.107.69.67:8081/images/20231209/1001/07_pam_001.jpg