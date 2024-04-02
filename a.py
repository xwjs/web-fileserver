# -*- coding: utf-8 -*-
from b import get_all ,zip_dir
from flask import Flask, send_file,render_template
import os

app = Flask(__name__)


ROOT='/home/cpp'
SHOW_DOT=True

@app.route('/file')
def list_files1():
    info=get_all(ROOT,'',SHOW_DOT)
    return render_template('index.html',files=info,path=ROOT)


@app.route('/file/<path:route>')
def list_files(route):

    info=get_all(ROOT,route,SHOW_DOT)
    return render_template('index.html',files=info,path=os.path.join(ROOT,route))

@app.route('/download/<path:filename>')
def dl_file(filename):

    path=os.path.join(ROOT,filename)
    if os.path.isdir(path):
        a,b=os.path.split(path)
        zip = zip_dir(a,b)

        response = send_file(zip,as_attachment=True)
        os.remove(zip)
        return response

    return send_file(os.path.join(ROOT,filename), as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

