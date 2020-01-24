from flask import Flask, render_template, request, make_response, flash, redirect
import urllib.parse as urlparse
from urllib.parse import parse_qs
from http import cookies
app = Flask(__name__,static_folder='static', static_url_path='')


@app.route('/')
def index():
    print("url nè "+ request.url)
    resp = make_response(render_template('index.html'))
    resp.set_cookie('gen', '4' )
    resp.set_cookie('legendary pokemon','true')
    resp.set_cookie('hint','find all')
    userAgent = request.headers.get('User-Agent')
    if (userAgent == 'Tajiri Satoshi'):
        return redirect('/flagTrue')
    return resp

@app.route('/flag.txt')
def flagFake():
    return render_template('flag.html')

@app.route('/arceus')
def arceus():
    return render_template('arceus.html')

@app.route('/dialga')
def dialga():
    return render_template('dialga.html')

@app.route('/giratina')
def giratina():
    return render_template('giratina.html')

@app.route('/palkia')
def palkia():
    return render_template('palkia.html')

@app.route('/flagTrue')
def flagTrue():
    return render_template('flagTrue.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 