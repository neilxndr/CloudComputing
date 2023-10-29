from flask import Flask, request, redirect, url_for
import boto3
import os

app = Flask(__name__)
s3 = boto3.client('s3')

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <body>
    <h1>Upload new File</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file"><br><br>
        <input type="submit" value="Upload">
    </form>
    </body>
    </html>
    '''

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        filename = file.filename
        if filename.endswith('.jpg'):
            folder = 'e-image/imagefile/'
        elif filename.endswith('.txt'):
            folder = 'e-image/textfile/'
        elif filename.endswith('.doc'):
            folder = 'e-image/docfile/'
        else:
            folder = 'e-image/other/'
        s3.put_object(Bucket='nap-news-agency-bucket', Key=folder + filename, Body=file)
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
