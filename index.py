#!/usr/bin/python3

from flask import Flask, render_template, redirect

from backend.parser.checksum import Checksum
from backend.parser.downloads import Downloads

app = Flask(__name__)

downloads = Downloads({
    'file': 'storage/example.pbd'
})

checksum = Checksum({
    'file': 'storage/example.pbd'
})

@app.route('/api')
def api():
    return downloads.list()

@app.route('/')
def index():
    return render_template(
        'index.html',
        
        site_name='Scimon: Hub'
    )

if __name__ == '__main__':
    app.run(debug=True)
