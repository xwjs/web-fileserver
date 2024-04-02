from b import get_all
from flask import Flask, send_file,render_template
import os
import zipfile

app = Flask(__name__)


ROOT='/home/cpp'
SHOW_DOT=True


@app.route('/file')
def list_files1():
    info=get_all(ROOT,'',SHOW_DOT)
    return render_template('index.html',files=info)


@app.route('/file/<path:route>')
def list_files(route):
    info=get_all(ROOT,route,SHOW_DOT)
    return render_template('index.html',files=info)

@app.route('/download/<filename>')
def dl_file(filename):
    return send_file(os.path.join(ROOT,filename), as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

