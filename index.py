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

@app.route('/')
def home():
    return checksum.get()

if __name__ == '__main__':
    app.run(debug=True)
