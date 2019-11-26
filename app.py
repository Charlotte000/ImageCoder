from flask import Flask, render_template, request, send_file
from ImageCoder import i2t, t2i

from PIL import Image
import base64
from io import BytesIO

import urllib.parse

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/text2img', methods=['GET'])
def text2img():
	# Decode text from bs64
	text = urllib.parse.unquote(request.args.get('data'))

	# Get code
	code = int(request.args.get('code'))

	# Process
	image = t2i(text, code)

	# Send image
	buffered = BytesIO()
	image.save(buffered, format="PNG")
	buffered.seek(0)
	return send_file(buffered, mimetype='image/PNG')

@app.route('/img2text', methods=['POST'])
def img2text():
	# Get code
	code = int(request.args.get('code'))

	# Get image
	image = Image.open(request.files['image'])

	# Process
	text = i2t(image, code)

	# Send text
	return text

# app.run()