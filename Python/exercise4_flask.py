# type: ignore

1xx 정보
2xx 성공
3xx 리다이렉트
4xx 클라이언트 에러
5xx 서버 에러

HEAD    리소스 정보 습득
GET     데이터 습득
POST    데이터 갱신
PUT     새 리소스 작성
DELETE

---------------------------------------------------------------------------flask1.html

from flask import Flask, render_template, request
import sqlalchemy

app = Flask(__name__, static_folder='.', static_url_path='', template_folder='.')

@app.route('/')
def home():
    return app.send_static_file('flask1.html')

@app.route('/<word>')
def echo(word):
    a = request.args.get('a')           # http://localhost:9999/good?a=1&b=2
    b = request.args.get('b')
    return render_template('flask1.html', **{'word': word, 'a': a, 'b': b})

app.run(port=9999, debug=True)

---------------------------------------------------------------------------flask2.html
""" flask_sqlalchemy
orm 사용, __init__ 자동 생성
preconfigured scoped session,
session의 remove는 자동
 """

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy, BaseQuery
import sqlalchemy as sa


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///.good-orm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = 'person'
    number = db.Column(sa.Integer, primary_key=True)
    name = db.Column(sa.String(10))
    age = db.Column(sa.Integer)

# Super class의 생성자를 override하고 싶은 경우 
# def __init__(**kwargs):
#     super(Person, self).__init__(**kwargs)
# 위와 같이 Super class의 생성자를 먼저 호출하고, 추가 작업 진행 """

    def __repr__(self):
        return f'<number: {self.number}, name: {self.name}, age: {self.age}>'
        

db.create_all()

person1 = Person(number=0, name='mg0', age=10)
person2 = Person(number=1, name='mg1', age=20)

session = db.session
session.add_all([person1, person2])
session.commit()

print(Person.query.all())