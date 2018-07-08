# -*- coding: utf-8 -*-

#!/usr/bin/python

import sys
from flask import Flask, request, jsonify, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
	return '''Hello, Flask Web Server.

		usage:
			/name
			/json
			/book
			/city
			/html
			/temp/html1
			/template/myname
			/image
			/gif
			/file
			/snowball
			/wechatappwebview
			/audio_1
			/audio_2
			/video_1
			/video_2
	'''

#use <user> to receive parameter
@app.route('/<name>')
def hello_to(name):
	return 'hello to %s' % name

@app.route('/hello/<user>')
def hello_get(user):
	return 'hello %s' % user

@app.route('/hello/<int:value>')
def hello_int(value):
	return 'hello %d' % (value + 1)


#post request
@app.route('/post/<user>', methods=['POST'])
def request_post(user):
	return 'request post %s' % user

@app.route('/request/<user>', methods=['GET', 'POST'])
def allRequest(user):
	print(request)
	print(request.args)
	print(request.form)
	if request.method == 'POST':
		return 'request post %s' % user
	return 'request get %s' % user

#json
@app.route('/json')
def json():
	return jsonify({
				'status': 0,
				'data': {
					'key1': 'value1',
					'key2': 'value2',
					'key3': 'value3'
				}
			})

@app.route('/book')
def book():
	return jsonify({
				'status': 0,
				'data': {
					'Title': 'My Title',
					'Author': 'My Author',
					'Content': 'My Content'
				}
			})

@app.route('/city')
def city():
	return jsonify({
				'status': 0,
				'data': {
					'Hubei': 'Xiangyang',
					'Shanghai': 'Shanghai',
					'Fujian': 'Xiamen'
				}
			})

#template
@app.route('/html')
def html():
	return render_template('html.html')

@app.route('/temp/<page>')
def temp(page):
	return render_template(page + '.html')

@app.route('/template/<name>')
def template(name):
	return render_template('template.html', name=name)

#image
@app.route('/image')
def image():
	imageName = 'files/image.png'
	return send_file(imageName, mimetype='image/png')

#gif
@app.route('/gif')
def gif():
	gifName = 'files/gif.gif'
	return send_file(gifName, mimetype='image/gif')

#file
@app.route('/file')
def file():
	fileName = 'file.json'
	return send_file(fileName, mimetype='text/json')

#audio
@app.route('/audio_1')
def audio_1():
	fileName = 'files/audio_1.mp3'
	return send_file(fileName, mimetype='audio/mp3')
@app.route('/audio_2')
def audio_2():
	fileName = 'files/audio_2.mp3'
	return send_file(fileName, mimetype='audio/mp3')

#video
@app.route('/video_1')
def video_1():
	fileName = 'files/video_1.mp4'
	return send_file(fileName, mimetype='video/mp4')
@app.route('/video_2')
def video_2():
	fileName = 'files/video_2.mp4'
	return send_file(fileName, mimetype='video/mp4')

#snowball
@app.route('/snowball')
def snowball():
	fileName = 'snowball.json'
	return send_file(fileName, mimetype='text/json')

@app.route('/wechatappwebview')
def wechatappwebview():
	return render_template('wechatappwebview.html')


if __name__ == '__main__':
	if len(sys.argv) == 1:
		app.run(host="0.0.0.0")
	else:
		port = int(sys.argv[1])
		app.run(host="0.0.0.0", port=port)
