from flask import Flask, render_template, request, send_file

import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html')