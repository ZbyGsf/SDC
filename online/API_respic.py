from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# 
IMAGE_FOLDER = 'your_image_folder_path'  #
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

app.logger.setLevel('DEBUG')

@app.route('/images/<path:subpath>/<filename>')
def get_image(subpath,filename):
    full_path = f"{app.config['UPLOAD_FOLDER']}/{subpath}"
    app.logger.info(f"Attempting to access: {full_path}")
    # 
    if os.path.exists(full_path):
        return send_from_directory(app.config['UPLOAD_FOLDER'],  f"{subpath}/{filename}")
    else:
        return "File not found", 404