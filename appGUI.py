from flask import Flask, request, render_template, redirect, url_for, send_from_directory
#from flask_ngrok import run_with_ngrok
from werkzeug.utils import secure_filename
import os
import cv2
import shutil
import time

def dir_last_updated(folder):
    return str(max(os.path.getmtime(os.path.join(root_path, f))
               for root_path, dirs, files in os.walk(folder)
               for f in files))

def make_overwritefolder(path):
    if os.path.exists(path):
        files = os.listdir(path)
        for file_name in files:
            file_path = path + '/' + file_name;
            os.remove(file_path)
    else:
        os.makedirs(path)

ALLOWED_EXTENSIONS = set(['jpg'])
plot_path = 'static/plot'
result_video_path = 'static/videos'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER # upload file
#run_with_ngrok(app)  # Start ngrok when app is run

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'GET':     
        return render_template('index.html')
             
    if request.method == 'POST':    
        list_plots = [ plot_path + '/' + i for i in os.listdir(plot_path)]
        return render_template('result.html', video_path='static/videos/ped2.mp4', list_plots=list_plots, dataset='ped2', last_updated=dir_last_updated('static'))

if __name__ == '__main__':
    app.run()
