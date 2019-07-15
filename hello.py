from flask import Flask,redirect,url_for,render_template


app = Flask(__name__)

movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]
@app.route('/已注册')
def hello():
    return '<h1>您已注册</h1><p>会员，您好！</p>'
@app.route('/未注册')
def hero():
    return redirect(url_for('create'))
@app.route('/注册界面')
def create():
    return '<h1>注册界面</h1><p>请如实填写您的用户信息，以便为您提供更全面的服务！</p>'
@app.route('/user/<int:age>')
def user(age):
    if age < 18:
        return 'You are only %d years old.SO FUCKING YOUNG!WATCH IT LATERRRRR!'%age
    else:
         return 'You are FUCKING old enough to watch it.'
@app.route('/<name>')
def azis(name):
    return render_template('index.html',name=name,movies=movies)