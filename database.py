# coding: utf-8

import config
import sys

import sqlalchemy as sa
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

config = config.rec()
engine = sa.create_engine(config.database + '?charset=utf8')

Session = sessionmaker()
Session.configure(bind = engine)
db = Session()

mBase = declarative_base()

def create_db():
    import models
    try:
        mBase.metadata.create_all(engine)
    except OperationalError, err:
        sys.stderr.write('OperationalError: %s\n' %  str(err))
        print("目测是数据库没有权限或不存在，自己不会看OpertaionalError啊混蛋！")
        sys.exit(1)
    print("数据库部署完成！")
    return
