from flask import Flask, render_template_string
import boto3

app = Flask(__name__)
s3 = boto3.client('s3')

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <body>
    <h1>News Agency File Browser</h1>
    <a href="/list/e-image/imagefile/">Image Files</a><br>
    <a href="/list/e-image/textfile/">Text Files</a><br>
    <a href="/list/e-image/docfile/">Doc Files</a><br>
    <a href="/list/e-image/other/"> Other Files </a><br>
    </body>
    </html>
    '''

@app.route('/list/<path:path>')
def list_files(path):
    response = s3.list_objects_v2(Bucket='nap-news-agency-bucket', Prefix=path)
    files = [obj['Key'] for obj in response['Contents']]
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <body>
        <h1>Files in {{ path }}</h1>
        {% for file in files %}
        <p>{{ file }}</p>
        {% endfor %}
        </body>
        </html>
        ''', path=path, files=files)

if __name__ == "__main__":
    app.run(port=5001, debug=True)
