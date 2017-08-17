# -*- coding: utf-8 -*-
import os
from flask import Flask, request
from flask_uploads import UploadSet, configure_uploads, IMAGES,\
 patch_request_class
import predict

app = Flask(__name__)
app.config['UPLOADED_PHOTOS_DEST'] = './cache'  # Uploads dir

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>RankFace</h1>
    <h5>via Entropy Xu</h5>
    <form method=post enctype=multipart/form-data>
         <input type=file name=photo>
         <input type=submit value=上传>
    </form>
    '''


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        # do the rank here
        outname = '#$' + filename
        predict.save_predict_img(photos.path(filename), './cache/' + outname)

        file_url = photos.url(outname)
        return html + '<br><img src=' + file_url + '>'
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
