from flask import Flask,redirect,url_for
app = Flask(__name__)
@app.route('/已注册')
def hello():
    return '<h1>您已注册</h1><p>会员，您好！</p>'
@app.route('/未注册')
def hero():
    return redirect(url_for('create'))
@app.route('/注册界面')
def create():
    return '<h1>注册界面</h1><p>请如实填写您的用户信息，以便为您提供更全面的服务！</p>'