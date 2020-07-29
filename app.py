from flask import Flask, request, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import cross_origin
from flask_cors import CORS

from dev import DEVConfig

app = Flask(__name__)
app.config.from_object(DEVConfig)
CORS(app, resources={r"/*": {"origins": "*"}}, send_wildcard=True)

# 初始化SQLAlchemy
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    # 数据库的基本操作
    name = data['name']
    email = data['email']
    print(name, email)
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
    return jsonify({'tasks': "来自flask的信息"})


@app.route('/hello/<username>')
def hey_user(username):
    return "hello! Mr %s" % username


@app.route('/test/my/first', methods=['POST'])
def first_post():
    try:
        my_json = request.get_json()
        print(my_json)
        get_name = my_json.get('name')
        get_age = my_json.get('age') + 20
        return jsonify(name=get_name, age=get_age)
    except Exception as e:
        print(e)
        return jsonify(msg='error!请检查参数')


@app.route('/try/login', methods=['POST'])
def login():
    pass


@app.route('/session', methods=['GET'])
def check_session():
    pass


if __name__ == '__main__':
    app.run()
