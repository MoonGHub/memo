DDL
    CREATE DATABASE dbname
    USE dbname
    DROP DATABASE dbname
    CREATE TABLE tbname(coldefs)
    TRUNCATE TABLE tbname       # 테이블 클리어

DML
    INSERT INTO tbname VALUES(....)
    SELECT ...
    UPDATE tbname SET col=value where condition
    DELETE from tbname where condition
--------------------------------------------------------------------------------

import sqlite3                      # 로컬 파일에 저장함
conn = sqlite3.connect('good.db')
curs = conn.cursor()                # 쿼리 수행자
curs.execute('CREATE TABLE IF NOT EXISTS good (id INTEGER(4), name VARCHAR(10), PRIMARY KEY(id, name))')

ins = 'INSERT INTO good (id, name) VALUES(?, ?)'
curs.execute(ins, (1, 'mg1'))
curs.execute(ins, (2, 'mg2'))
curs.executemany(ins, [(3, 'mg3'), (4, 'mg4')])
conn.commit()

sel = 'SELECT * FROM good'
print(curs.execute(sel).fetchall())

curs.close()
conn.close()

--------------------------------------------------------------------------------
ORM(Object Reletional Mapping) 사용
dialect(db타입)+driver://user:passwrod@host:port/dbname

import sqlalchemy as sa
conn = sa.create_engine('sqlite:///good.db')     # /패스는 실행 프로그램 기준, dbname 생략 시, 메모리에 생성, 
conn: sa.engine.Engine                          # 자동완성이 안되서 설정, 타입으로 지정해 참조하는 듯
conn.execute('CREATE TABLE IF NOT EXISTS good (id INTEGER(4), name VARCHAR(10), PRIMARY KEY(id, name))')
ins = 'INSERT INTO good (id, name) VALUES(?, ?)'
conn.execute(ins, (1, 'mg1'))
for row in conn.execute('SELECT * FROM good'):
    print(row)

-----------------------------------------

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
conn = sa.create_engine('sqlite:///.good-orm.db')
Base = declarative_base()
Base: sa.schema.Table                       # 자동완성.

class Man(Base):
    __tablename__ = 'man'
    name = sa.Column('name', sa.String, primary_key=True)
    age = sa.Column('age', sa.Integer, primary_key=True)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'name : {self.name}, age : {self.age}'

Base.metadata.create_all(conn)

man_list = [Man('mg1', 10), Man('mg2', 20), Man('mg3', 30)]

Session = sa.orm.sessionmaker(bind=conn)
session = Session()
session: sa.orm.Session

session.add_all(man_list)
session.commit()

for row in session.execute('SELECT * FROM man'):
    print(row)
session.close()

--------------------------------------------------------------------------------
Redis 259p, 342p, 349p(pub, sub - 기타.. zmq, RabbitMQ)

