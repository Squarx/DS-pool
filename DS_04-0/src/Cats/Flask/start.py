import base64
import sys
import this

from PIL import Image
import io
from collections import namedtuple
from flask import Flask
from flask import render_template, redirect, url_for, request
from bs4 import BeautifulSoup

sys.path.append("..")
from api_class.my_class import Web1

app = Flask(__name__)
app.run(debug=True)
Message = namedtuple('Message', 'text tag')
messages = []
cats = []


# https://flask.palletsprojects.com/en/2.2.x/quickstart/?highlight=quickstart
# to start: python3 -m flask  --app start run
# site http://127.0.0.1:5000
@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route("/main", methods=['GET'])
def main():
    return render_template('main.html', messages=messages)


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']
    messages.append(Message(text, tag))
    return redirect(url_for('main'))


# @app.route('/test', methods=['POST'])
# def test():
#     t = Web1()
#     text = str(t.get_num())
#     tag = 'Add cat'
#     messages.append(Message(text, tag))
#     return redirect(url_for('main'))


@app.route('/main', methods=['POST'])
def hello_hell():
    num = request.form['num']
    t = Web1(404)
    try:
        t = Web1(int(num))
    except ValueError:
        t = Web1(101)
        messages.append(Message('Incrrect input', num))
    im = t.get_image()
    data = io.BytesIO()
    im.save(data, "JPEG")
    encoded_img_data = base64.b64encode(data.getvalue())
    return render_template("main.html", img_data=encoded_img_data.decode('utf-8'), messages=messages)


@app.route('/update', methods=['POST', 'GET'])
def print_cat():
    # redirect('/maiasdasadn/')
    image_src = ""
    with open('templates/main.html', 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        image_src = soup.find('img')['src']
    tmp = Web1()
    # tem_img = request.form['IMG']
    # print(type(tem_img))
    redirect(url_for('main'))
    print("works")
    return render_template("main.html", cats=tmp.print_available_list(), img_data=image_src)
