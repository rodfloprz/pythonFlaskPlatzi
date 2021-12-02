from flask import Flask, request, redirect, make_response

app = Flask(__name__)

@app.route('/')
def index():
    user_ip=request.remote_addr
    response=make_response(redirect('/hello'))
    response.set_cookie('user_ip',user_ip)

    return response

@app.route('/hello')
def hello():
    user_ip=request.cookies.get('user_ip')
    return "Hello world Python, tu IP es: {}".format(user_ip)